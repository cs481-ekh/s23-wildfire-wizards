import React, { useEffect, useState } from "react";
import { MapContainer, TileLayer, Circle, Popup } from "react-leaflet";
import Select from "react-select";
//import Select from '@mui/material/Select'
import Slider from "@mui/material/Slider";
//import { HeatmapLayer } from "react-leaflet-heatmap-layer-v3";
import axios from "axios";
import "./../styles.css";
import logo from "./../components/sdp_logo_fire.png";
import { Link } from "react-router-dom";
import JSPopup from "reactjs-popup";
import "reactjs-popup/dist/index.css";
import Box from "@mui/material/Box";
import Grid from "@mui/material/Grid";
import Typography from "@mui/material/Typography";
import MuiInput from "@mui/material/Input";
import { styled } from "@mui/material/styles";
import OutlinedInput from "@mui/material/OutlinedInput";
import Button from "@mui/material/Button";
import Modal from "@mui/material/Modal";
import CircularProgress from "@mui/material/CircularProgress";
import Radio from "@mui/material/Radio";
import RadioGroup from "@mui/material/RadioGroup";
import FormControlLabel from "@mui/material/FormControlLabel";
import FormControl from "@mui/material/FormControl";
import { HeatmapLayer } from "react-leaflet-heatmap-layer-v3";
import Checkbox from '@mui/material/Checkbox';
import FormGroup from '@mui/material/FormGroup';
//import { Tooltip } from "leaflet";
import Tooltip from '@mui/material/Tooltip';
import { getAllCategories, getFields } from "../Helpers";
import { createTheme, ThemeProvider } from '@mui/material/styles';


const toolTipTheme = createTheme({
  components: {
    MuiTooltip: {
      styleOverrides: {
        tooltip: {
          fontSize: '17px',
          maxWidth: '300px',
          padding: '6px',
        },
      },
    },
  },
});


const modalStyle = {
  position: "absolute",
  top: "50%",
  left: "50%",
  transform: "translate(-50%, -50%)",
  bgcolor: "background.paper",
  border: "2px solid #000",
  boxShadow: 24,
  p: 4,
};

const categoriesInitial = ["FPA_FOD", 
  "Annual Climate", "Cheat Grass", "Climate Normals", "GRIDMET", 
  "Climate Percentiles", "Ecoregions", "Topography", "Vegetation",
  "Risk Management Assistance", "Fire Regime Groups", "Fire Stations", 
  "Geographic Area Coordination Centers", "Gap Analysis Project", 
  "Gross Domestic Product", "Global Human Modification", "MODIS NDVI", 
  "NOAA NDVI", "National Land Cover Database", "National Preparedness Level", "Population", "Pyrome", "Road", 
  "Social Vulnerability Index", "Rangeland Production Monitoring Service",  "Climate and Economic Justice Screening Tool"];

const categoriesAbvInitial = ["FPA_FOD",  
  "Annual Climate", "Cheat Grass", "Climate Normals", "GRIDMET", 
  "Climate Percentiles", "Ecoregions", "Topography", "Vegetation",
  "RMA", "Fire Regime Groups", "Fire Stations", 
  "GACC", "Gap Analysis Project", 
  "GDP", "GHM", "MODIS NDVI", 
  "NOAA NDVI", "NLCD", "NPL", "Population", "Pyrome", "Road", 
  "SVI", "RPMS", "CEJST"];

const selectedFieldsInitial = ["FOD_ID", "FPA_ID", "FIRE_NAME", "FIRE_SIZE", "DISCOVERY_DATE", 
  "LATITUDE", "LONGITUDE", "NWCG_CAUSE_CLASSIFICATION"];

const possible_states = [
  'AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE','FL', 'GA', 'HI',
  'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD','ME','MI', 'MN', 
  'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH',
  'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VT',
  'WA', 'WI', 'WV', 'WY'
  ] // 50 states + DC and PR in alphabetical order by code

const Data = () => {
  const [stateChoice, setStateChoice] = useState();
  const [countyChoice, setCountyChoice] = useState();
  const [yearChoice, setYearChoice] = useState();
  const [countyList, setCountyList] = useState([]);
  const [stateList, setList] = useState([]);
  const [variableList, setVariableList] = useState([]);
  const [yearsList, setYearsList] = useState([]);
  const [viewType, setViewType] = useState("points");
  const [doyChoiceLTE, setDoyChoiceLTE] = useState(366);
  const [doyChoiceGTE, setDoyChoiceGTE] = useState(1);
  const [sizeChoiceLTE, setSizeChoiceLTE] = useState();
  const [sizeChoiceGTE, setSizeChoiceGTE] = useState();
  const [results, setResults] = useState([]);
  const [isWarningExpanded, setWarningVisible] = useState(false);
  const [modalVisible, setModalVisible] = useState(false);
  const [modalData, setModalData] = useState([]);
  const [loading, setLoading] = useState(false);
  const [categoriesChoice, setCategoriesChoice] = useState([]); 
  const [selectedCheckboxes, setSelectedCheckboxes] = useState([]);
  const [selectedFields, setSelectedFields] = useState(selectedFieldsInitial);
  const [isSelectAll, setIsSelectAll] = useState(false);
  const [allCountyLists, setCountyLists] = useState({});
  const [categories, setCategories] = useState(getAllCategories());
  const [categories_abv, setCatAbv] = useState(categoriesAbvInitial);

  const handleClose = () => setModalVisible(false);

  const Input = styled(MuiInput)`
    width: 42px;
  `;
  const [value, setValue] = React.useState(1);
  const [valueLTE, setValueLTE] = React.useState(1);
  const [doubleValue, setDoubleValue] = React.useState([1, 366]);
  const handleSliderChange = (event, newValue) => {
    setValue(newValue);
  };
  const handleSliderChangeGTE = (event, newValue) => {
    setValue(newValue);
    setDoyChoiceGTE(Number(event.target.value));
  };
  const handleSliderChangeLTE = (event, newValue) => {
    setValueLTE(newValue);
    setDoyChoiceLTE(Number(event.target.value));
  };
  const handleBlur = () => {
    if (value < 0) {
      setValue(0);
    } else if (value > 366) {
      setValue(366);
    }
  };
  const testSliderChange = (event, newValue) => {
    setDoubleValue(handleSliderChangeGTE, handleInputChangeLTE);
  };
  const handleInputChange = (event) => {
    setValue(event.target.value === "" ? "" : Number(event.target.value));
  };
  const handleInputChangeGTE = (event) => {
    setValue(event.target.value === "" ? "" : Number(event.target.value));
    setDoyChoiceGTE(Number(event.target.value));
  };

  const handleInputChangeLTE = (event) => {
    setValueLTE(event.target.value === "" ? "" : Number(event.target.value));
    setDoyChoiceLTE(Number(event.target.value));
  };

  const setSizeChoiceGTEInput = (event) => {
    //setValueLTE(event.target.value === '' ? '' : Number(event.target.value));
    setSizeChoiceGTE(Number(event.target.value));
  };

  const setSizeChoiceLTEInput = (event) => {
    //setValueLTE(event.target.value === '' ? '' : Number(event.target.value));
    setSizeChoiceLTE(Number(event.target.value));
  };

  const [searchCount, setSearchCount] = useState(0);
  const [searchTime, setSearchTime] = useState(0);

  useEffect(
    () => {
      // data will not change between page loads, don't reload it
      if (stateList.length === 0) {
        refreshList(stateList, "distinct_states_list/", "s");
      }
      if (yearsList.length === 0) {
        refreshList(yearsList, "distinct_years_list/", "y");
      }
      getCountyLists();
    },
    /* This makes sure we run this once */
    []
  );

  async function getFireDetails(id) {
    const headers = {
      Accept: "application/json",
    };
    console.log("fetching fire details");
    const response = await axios.get(
      process.env.REACT_APP_DJANGO_API_URL + "fire/",
      {
        params: {
          FOD_ID: id,
        },
        headers: headers,
      }
    );
    console.log(response.data[0]);
    setModalData(response.data[0]);
  }

  async function refreshList(alist, aroute, w) {
    try {
      // django could return html if it wanted, request json specifically
      const headers = {
        Accept: "application/json",
      };
      //Axios to send and receive HTTP requests
      console.log("requesting list");
      const response = await axios.get(
        process.env.REACT_APP_DJANGO_API_URL + aroute,
        { headers }
      );
      alist = [];
      let names = await response.data;
      names.forEach((item) => {
        alist.push(item);
      });

      //s indicates we want a state list to update
      if (w === "s") {
        const sList = alist.map((item) => {
          var nitem = {
            label: item,
            value: item,
          };
          return nitem;
        });
        setList(sList);
      }
      //county list update
      /*else if (w === "c") {
        const sList = alist.map((item) => {
          var nitem = {
            label: item,
            value: item,
          };
          return nitem;
        });
        setCountyList(sList);
      }*/
      //years list update
      else if (w === "y") {
        const sList = alist.map((item) => {
          var nitem = {
            label: item,
            value: item,
          };
          return nitem;
        });
        setYearsList(sList);
      }
      //why is useState showing one state change behind in console???
      ///HELP??
      // console.log(stateList);
      // console.log(countyList);
    } catch (e) {
      //DEBUG
      console.log("error requesting state/county list");
      console.log(e);
    }
  }

  async function getCountyLists() {
    possible_states.forEach(async (stateCode) =>{
      let route = "distinct_counties_list/?STATE="+stateCode;
      try {
        // django could return html if it wanted, request json specifically
        const headers = {
          Accept: "application/json",
        };
        //Axios to send and receive HTTP requests
        console.log("requesting list");
        const response = await axios.get(
          process.env.REACT_APP_DJANGO_API_URL + route,
          { headers }
        );
        let rData = await response.data;
        let counties = [];
        rData.forEach((c) => {
          var nitem = {
            label: c,
            value: c,
          };
          counties.push(nitem);
        })
        allCountyLists[stateCode] = counties;
        setCountyLists(allCountyLists);
      } catch (e) {
        console.log("error requesting county lists");
        console.log(e);
      }
    })
  }

  const refreshCountyList = (stateCode) => {
    setCountyList(allCountyLists[stateCode]);
    /*let route = "distinct_counties_list/?STATE="+stateCode;
    try {
      // django could return html if it wanted, request json specifically
      const headers = {
        Accept: "application/json",
      };
      //Axios to send and receive HTTP requests
      console.log("requesting list");
      const response = await axios.get(
        process.env.REACT_APP_DJANGO_API_URL + route,
        { headers }
      );
      let rData = await response.data;
      let counties = [];
      rData.forEach((c) => {
        var nitem = {
          label: c,
          value: c,
        };
        counties.push(nitem);
      })
      setCountyList(counties);
    } catch (e) {
      console.log("error requesting state/county list");
      console.log(e);
    }*/
  }

  async function refreshVariableList(alist, aroute) {
    try {
      const headers = {
        Accept: "application/json",
      };
      console.log("requesting variable list");
      const response = await axios.get(
        process.env.REACT_APP_DJANGO_API_URL + aroute,
        { headers }
      );
      alist = [];
      let names = await response.data;
      for (const [key, description] of Object.entries(names)) {
        var item = { label: key, value: description };
        alist.push(item);
      }
      const vList = alist;
      console.log(vList);
      setVariableList(vList);
    } catch (e) {
      console.log("error requesting variable list");
      console.log(e);
    }
  }

  const handleStateChange = (obj) => {
    setStateChoice(obj);
    //setCountyList(obj.value);
    //setCounty(null);
    refreshCountyList(obj.value);
    console.log(stateChoice);
    console.log(stateList);
  };

  // handle change event of the language dropdown
  const handleCountyChange = (obj) => {
    setCountyChoice(obj);
  };

  const handleYearChoiceChange = (obj) => {
    setYearChoice(obj);
  };

  const acresToMetersRadius = (acres) => {
    //r = √(A / π)
    return Math.sqrt(
      // acres to sq meters (approx)
      (acres * 4046) / 3
    );
  };

  async function handleSearch() {
    if (checkIfEnoughFilter()) {
      setWarningVisible(false);
      setLoading(true);
      console.log(yearChoice);
      setSearchTime(0);
      var startTime = performance.now();
      try {
        // django could return html if it wanted, request json specifically
        const headers = {
          Accept: "application/json",
        };
        const params = {
          ...(yearChoice && { FIRE_YEAR: yearChoice.value }),
          ...(doyChoiceGTE && { DISCOVERY_DOY__gte: doyChoiceGTE }),
          ...(doyChoiceLTE && { DISCOVERY_DOY__lte: doyChoiceLTE }),
          ...(stateChoice && { STATE: stateChoice.value }),
          ...(countyChoice && { COUNTY: countyChoice.value }),
          ...(sizeChoiceGTE && { FIRE_SIZE__gte: sizeChoiceGTE }),
          ...(sizeChoiceLTE && { FIRE_SIZE__lte: sizeChoiceLTE }),
          ...(categoriesChoice && {CATEGORIES: categoriesChoice}),
        };
        console.log("params:");
        console.log(params);
        //Axios to send and receive HTTP requests
        const response = await axios.get(
          process.env.REACT_APP_DJANGO_API_URL + "search/",
          { params: params, headers: headers }
        );
        console.log("requesting");
        const data = await response.data;
        console.log(response);
        console.log(data);
        setSearchCount(data.length);
        setResults(data);
      } catch (e) {
        console.log(e);
      }
      var endTime = performance.now();
      var timeDiff = (endTime - startTime) / 1000;
      setSearchTime(timeDiff);
      setLoading(false);
    } else {
      setWarningVisible(true);
    }
  }

  async function handleDownloadCSV() {
    const searchParams = new URLSearchParams();
    if (yearChoice) {
      searchParams.append("FIRE_YEAR", yearChoice.value);
    }
    if (doyChoiceGTE) {
      searchParams.append("DISCOVERY_DOY__gte", doyChoiceGTE);
    }
    if (doyChoiceLTE) {
      searchParams.append("DISCOVERY_DOY__lte", doyChoiceLTE);
    }
    if (stateChoice) {
      searchParams.append("STATE", stateChoice.value);
    }
    if (countyChoice) {
      searchParams.append("COUNTY", countyChoice.value);
    }
    if (sizeChoiceGTE) {
      searchParams.append("FIRE_SIZE__gte", sizeChoiceGTE);
    }
    if (sizeChoiceLTE) {
      searchParams.append("FIRE_SIZE__lte", sizeChoiceLTE);
    }
    if(categoriesChoice) { 
      searchParams.append("CATEGORIES", categoriesChoice);
    }

    window.open(
      process.env.REACT_APP_DJANGO_API_URL +
        "subset_csv/?" +
        searchParams.toString(),
      "_blank",
      "noopener,noreferrer"
    );
  }

  const handleViewChange = (event) => {
    setViewType(event.target.value);
  };

  const checkIfEnoughFilter = () => {
    var points = 0;

    if (yearChoice) {
      points += 1;
    }
    if (stateChoice) {
      points += 1;
    }
    if (doyChoiceLTE - doyChoiceGTE <= 50) {
      points += 1;
    }
    if (sizeChoiceGTE > 1000) {
      points += 1;
    }

    if (points >= 2) {
      console.log("adequate filters");
      return true;
    }
    console.log("inadequate filters");
    return false;
  };

  const handleCategoryChange = (event) => { 
    let index = selectedCheckboxes.indexOf(event.target.name);
    if(index>=0){
      selectedCheckboxes.splice(index, 1)
      setCategories(getAllCategories())
      setSelectedCheckboxes(selectedCheckboxes);
    }else{
      selectedCheckboxes.push(event.target.name)
      setSelectedCheckboxes(selectedCheckboxes);
    }
    setCategoriesChoice(selectedCheckboxes);
    if(selectedCheckboxes.length>0){
      setSelectedFields(getFields(selectedCheckboxes));
    }else{
      setSelectedFields(selectedFieldsInitial);
    }
    if(selectedCheckboxes.length==categories.length){
      setIsSelectAll(true);
    }else{
      setIsSelectAll(false);
    }
  };

  const handleSelectAll = () => {
    if(!isSelectAll){
      setSelectedCheckboxes(getAllCategories());
      setCategoriesChoice(getAllCategories());
      setSelectedFields(getFields(getAllCategories()));
    }else{
      setSelectedCheckboxes([]);
      setCategoriesChoice([]);
      setSelectedFields(selectedFieldsInitial);
    }
    setCategories(getAllCategories())
    setIsSelectAll(!isSelectAll);
  };

  return (
    <div className="data_container">
      <div
        className="data_sidebar"
        style={{
          width: 400,
          position: "relative",
          top: 0,
          left: 0,
        }}
      >
        <JSPopup
          trigger={<Link>⚠️ Important Notice ⚠️</Link>}
          position="bottom center"
        >
          <div>
            Results with more than 10,000 fires on the map at a time can cause
            poor browser performance.
            <br />
            For this reason, you may be disallowed from a broad search of fires.
            <br />
            For the best experience, filter your search to be as detailed as
            possible.
          </div>
        </JSPopup>
        <div
          style={{
            overflow: "scroll",
            width: "auto",
            marginTop: 20,
            marginBottom: 20,
            padding: 20,
            maxHeight: "70vh",
            border: "1px solid #000",
            borderRadius: "0px",
          }}
        >
          <div title="Calendar year in which the fire was discovered or confirmed to exist">
            YEAR:
          </div>
          <Select
            placeholder="-Select Year-"
            isClearable={true}
            value={yearChoice}
            options={yearsList}
            onChange={handleYearChoiceChange}
            getOptionLabel={(x) => x.label}
            getOptionValue={(x) => x.value}
          />
          <br />
          <div title="Two-letter alphabetic code for the state in which the fire burned (or originated), based on the nominal designation in the fire report">
            STATE:
          </div>
          <Select
            placeholder="-Select State-"
            isClearable={true}
            value={stateChoice}
            options={stateList}
            onChange={handleStateChange}
            getOptionLabel={(x) => x.label}
            getOptionValue={(x) => x.value}
          />
          <br />
          <div title="County, or equivalent, in which the fire burned (or originated), based on nominal designation in the fire report">
            COUNTY:
          </div>
          <Select
            placeholder="-Select County-"
            isClearable={true}
            value={countyChoice}
            options={countyList}
            onChange={handleCountyChange}
            getOptionLabel={(x) => x.label}
            getOptionValue={(x) => x.value}
          />
          <br />
          <div title="Day of year on which the fire was discovered or confirmed to exist" style={{ fontSize: "12px", fontWeight: "bold"}}>
            DISCOVERY DAY OF YEAR:
          </div>
          <div>Greater than or equal to:</div>
          <Box sx={{ flexGrow: 1, display: { xs: "flex", md: "flex" } }}>
            <Grid container spacing={2} alignItems="center">
              <Grid item></Grid>
              <Grid item xs>
                <Slider
                  value={doyChoiceGTE ? doyChoiceGTE : 1}
                  onChange={handleSliderChangeGTE}
                  min={1}
                  max={doyChoiceLTE ? doyChoiceLTE : 366}
                  aria-labelledby="input-slider"
                />
              </Grid>
              <Grid item>
                <OutlinedInput
                  value={value}
                  size="small"
                  onChange={handleInputChangeGTE}
                  onBlur={handleBlur}
                  inputProps={{
                    step: 10,
                    min: 1,
                    max: doyChoiceLTE ? doyChoiceLTE : 366,
                    type: "number",
                    "aria-labelledby": "input-slider",
                  }}
                />
              </Grid>
            </Grid>
          </Box>
          <div>Less than or equal to:</div>
          <Box sx={{ flexGrow: 1, display: { xs: "flex", md: "flex" } }}>
            <Grid container spacing={2} alignItems="center">
              <Grid item></Grid>
              <Grid item xs>
                <Slider
                  value={doyChoiceLTE ? doyChoiceLTE : 366}
                  onChange={handleSliderChangeLTE}
                  min={doyChoiceGTE ? doyChoiceGTE : 1}
                  max={366}
                  aria-labelledby="input-slider"
                />
              </Grid>
              <Grid item>
                <OutlinedInput
                  value={doyChoiceLTE ? doyChoiceLTE : 366}
                  size="small"
                  onChange={handleInputChangeLTE}
                  onBlur={handleBlur}
                  inputProps={{
                    step: 10,
                    min: doyChoiceGTE ? doyChoiceGTE : 1,
                    max: 366,
                    type: "number",
                    "aria-labelledby": "input-slider",
                  }}
                />
              </Grid>
            </Grid>
          </Box>
          <br />
          <div title="The estimate of acres within the final perimeter of the fire">
            FIRE SIZE:
          </div>
          <div>Greater than or equal to:</div>
          <br />
          <Box sx={{ flexGrow: 1, display: { xs: "flex", md: "flex" } }}>
            <Grid
              container
              spacing={2}
              alignItems="center"
              justifyContent="center"
            >
              <Grid alignItems="center">
                <OutlinedInput
                  sx={{ width: 200 }}
                  variant="outlined"
                  value={sizeChoiceGTE ? sizeChoiceGTE : 0}
                  size="small"
                  inputProps={{
                    step: 1,
                    min: 0,
                    max: sizeChoiceLTE ? sizeChoiceLTE : 999999999,
                    type: "number",
                    "aria-labelledby": "input-slider",
                  }}
                  onChange={setSizeChoiceGTEInput}
                  endAdornment="acres"
                />
              </Grid>
            </Grid>
          </Box>
          <br />
          MAP VIEW:
          <br />
          <Grid
            container
            spacing={2}
            alignItems="center"
            justifyContent="center"
          >
            <Grid alignItems="center" marginTop={2}>
              <FormControl>
                <RadioGroup
                  aria-labelledby="demo-radio-buttons-group-label"
                  defaultValue="female"
                  name="radio-buttons-group"
                  value={viewType}
                  onChange={handleViewChange}
                >
                  <FormControlLabel
                    value="points"
                    control={<Radio />}
                    label="Points"
                  />
                  <FormControlLabel
                    value="heatmap"
                    control={<Radio />}
                    label="Heatmap"
                  />
                </RadioGroup>
              </FormControl>
            </Grid>
          </Grid>
          <br />
          <div title="subcategory selector">
            ATTRIBUTE CATEGORIES TO DOWNLOAD: 
          </div>
          <Button
            onClick={() => {
              window
                .open(
                  "https://docs.google.com/spreadsheets/d/1Or4V3SxyUu4vsBbMkop66Dt7Rzq4_UDv/edit?usp=sharing&ouid=108049105554866139180&rtpof=true&sd=true",
                  "_blank"
                )
                .focus();
            }}
          >
            About our variables
          </Button>
          <br />
            <Grid
              container
              spacing={0.5}
              alignItems="left"
              justifyContent="left"
            >
              <Grid alignItems="left">
                <FormControl>
                  <FormGroup
                    name="checkbox-group"
                  >
                    <>
                      <FormControlLabel control={<Checkbox onChange={handleSelectAll} name="Select All" checked={isSelectAll} />} label="Select All" />
                    </>
                    <ThemeProvider theme={toolTipTheme}>
                    <Tooltip title={categories[0]} placement="right">
                      <FormControlLabel control={<Checkbox onChange={handleCategoryChange} name={categories[0]} checked={selectedCheckboxes.indexOf(categories[0])>=0 || isSelectAll} />} label={categories_abv[0]} />
                    </Tooltip>
                    <Tooltip title={categories[1]} placement="right">
                      <FormControlLabel control={<Checkbox onChange={handleCategoryChange} name={categories[1]} checked={selectedCheckboxes.indexOf(categories[1])>=0 || isSelectAll} />} label={categories_abv[1]} />
                    </Tooltip>
                    <Tooltip title={categories[2]} placement="right">
                      <FormControlLabel control={<Checkbox onChange={handleCategoryChange} name={categories[2]} checked={selectedCheckboxes.indexOf(categories[2])>=0 || isSelectAll} />} label={categories_abv[2]} />
                    </Tooltip>
                    <Tooltip title={categories[3]} placement="right">
                      <FormControlLabel control={<Checkbox onChange={handleCategoryChange} name={categories[3]} checked={selectedCheckboxes.indexOf(categories[3])>=0 || isSelectAll} />} label={categories_abv[3]} />
                    </Tooltip>
                    <Tooltip title={categories[4]} placement="right">
                      <FormControlLabel control={<Checkbox onChange={handleCategoryChange} name={categories[4]} checked={selectedCheckboxes.indexOf(categories[4])>=0 || isSelectAll} />} label={categories_abv[4]} />
                    </Tooltip>
                    <Tooltip title={categories[5]} placement="right">
                      <FormControlLabel control={<Checkbox onChange={handleCategoryChange} name={categories[5]} checked={selectedCheckboxes.indexOf(categories[5])>=0 || isSelectAll} />} label={categories_abv[5]} />
                    </Tooltip>
                    <Tooltip title={categories[6]} placement="right">
                      <FormControlLabel control={<Checkbox onChange={handleCategoryChange} name={categories[6]} checked={selectedCheckboxes.indexOf(categories[6])>=0 || isSelectAll} />} label={categories_abv[6]} />
                    </Tooltip>
                    <Tooltip title={categories[7]} placement="right">
                      <FormControlLabel control={<Checkbox onChange={handleCategoryChange} name={categories[7]} checked={selectedCheckboxes.indexOf(categories[7])>=0 || isSelectAll} />} label={categories_abv[7]} />
                    </Tooltip>
                    <Tooltip title={categories[8]} placement="right">
                      <FormControlLabel control={<Checkbox onChange={handleCategoryChange} name={categories[8]} checked={selectedCheckboxes.indexOf(categories[8])>=0 || isSelectAll} />} label={categories_abv[8]} />
                    </Tooltip>
                    <Tooltip title={categories[9]} placement="right">
                      <FormControlLabel control={<Checkbox onChange={handleCategoryChange} name={categories[9]} checked={selectedCheckboxes.indexOf(categories[9])>=0 || isSelectAll} />} label={categories_abv[9]} />
                    </Tooltip>
                    <Tooltip title={categories[10]} placement="right">
                      <FormControlLabel control={<Checkbox onChange={handleCategoryChange} name={categories[10]} checked={selectedCheckboxes.indexOf(categories[10])>=0 || isSelectAll} />} label={categories_abv[10]} />
                    </Tooltip>
                    <Tooltip title={categories[11]} placement="right">
                      <FormControlLabel control={<Checkbox onChange={handleCategoryChange} name={categories[11]} checked={selectedCheckboxes.indexOf(categories[11])>=0 || isSelectAll} />} label={categories_abv[11]} />
                    </Tooltip>
                    <Tooltip title={categories[12]} placement="right">
                      <FormControlLabel control={<Checkbox onChange={handleCategoryChange} name={categories[12]} checked={selectedCheckboxes.indexOf(categories[12])>=0 || isSelectAll} />} label={categories_abv[12]} />
                    </Tooltip>
                    <Tooltip title={categories[13]} placement="right">
                      <FormControlLabel control={<Checkbox onChange={handleCategoryChange} name={categories[13]} checked={selectedCheckboxes.indexOf(categories[13])>=0 || isSelectAll} />} label={categories_abv[13]} />
                    </Tooltip>
                    <Tooltip title={categories[14]} placement="right">
                      <FormControlLabel control={<Checkbox onChange={handleCategoryChange} name={categories[14]} checked={selectedCheckboxes.indexOf(categories[14])>=0 || isSelectAll} />} label={categories_abv[14]} />
                    </Tooltip>
                    <Tooltip title={categories[15]} placement="right">
                      <FormControlLabel control={<Checkbox onChange={handleCategoryChange} name={categories[15]} checked={selectedCheckboxes.indexOf(categories[15])>=0 || isSelectAll} />} label={categories_abv[15]} />
                    </Tooltip>
                    <Tooltip title={categories[16]} placement="right">
                      <FormControlLabel control={<Checkbox onChange={handleCategoryChange} name={categories[16]} checked={selectedCheckboxes.indexOf(categories[16])>=0 || isSelectAll} />} label={categories_abv[16]} />
                    </Tooltip>
                    <Tooltip title={categories[17]} placement="right">
                      <FormControlLabel control={<Checkbox onChange={handleCategoryChange} name={categories[17]} checked={selectedCheckboxes.indexOf(categories[17])>=0 || isSelectAll} />} label={categories_abv[17]} />
                    </Tooltip>
                    <Tooltip title={categories[18]} placement="right">
                      <FormControlLabel control={<Checkbox onChange={handleCategoryChange} name={categories[18]} checked={selectedCheckboxes.indexOf(categories[18])>=0 || isSelectAll} />} label={categories_abv[18]} />
                    </Tooltip>
                    <Tooltip title={categories[19]} placement="right">
                      <FormControlLabel control={<Checkbox onChange={handleCategoryChange} name={categories[19]} checked={selectedCheckboxes.indexOf(categories[19])>=0 || isSelectAll} />} label={categories_abv[19]} />
                    </Tooltip>
                    <Tooltip title={categories[20]} placement="right">
                      <FormControlLabel control={<Checkbox onChange={handleCategoryChange} name={categories[20]} checked={selectedCheckboxes.indexOf(categories[20])>=0 || isSelectAll} />} label={categories_abv[20]} />
                    </Tooltip>
                    <Tooltip title={categories[21]} placement="right">
                      <FormControlLabel control={<Checkbox onChange={handleCategoryChange} name={categories[21]} checked={selectedCheckboxes.indexOf(categories[21])>=0 || isSelectAll} />} label={categories_abv[21]} />
                    </Tooltip>
                    <Tooltip title={categories[22]} placement="right">
                      <FormControlLabel control={<Checkbox onChange={handleCategoryChange} name={categories[22]} checked={selectedCheckboxes.indexOf(categories[22])>=0 || isSelectAll} />} label={categories_abv[22]} />
                    </Tooltip>
                    <Tooltip title={categories[23]} placement="right">
                      <FormControlLabel control={<Checkbox onChange={handleCategoryChange} name={categories[23]} checked={selectedCheckboxes.indexOf(categories[23])>=0 || isSelectAll} />} label={categories_abv[23]} />
                    </Tooltip>
                    <Tooltip title={categories[24]} placement="right">
                      <FormControlLabel control={<Checkbox onChange={handleCategoryChange} name={categories[24]} checked={selectedCheckboxes.indexOf(categories[24])>=0 || isSelectAll} />} label={categories_abv[24]} />
                    </Tooltip>
                    <Tooltip title={categories[25]} placement="right">
                      <FormControlLabel control={<Checkbox onChange={handleCategoryChange} name={categories[25]} checked={selectedCheckboxes.indexOf(categories[25])>=0 || isSelectAll} />} label={categories_abv[25]} />
                    </Tooltip>
                    </ThemeProvider>
                  </FormGroup>
                </FormControl>
              </Grid>
            </Grid>
          <br />
        </div>
        <JSPopup
          trigger={<Link>ℹ️ Search Tips ℹ️</Link>}
          position="top center"
        >
          <div>
            If you decide to change the attribute categories, you don't need to search again to see the new categories in a fire's Additional Details.
          </div>
        </JSPopup>
        <br />
        {loading && (
          <div>
            <CircularProgress />
          </div>
        )}
        {isWarningExpanded && (
          <div style={{ color: "red" }}>
            Unable to process your request due to lack of adequate fiters.
            <br />
            Please filter your search further.
          </div>
        )}
        <Button variant="contained" onClick={handleSearch}>
          Search
        </Button>
        <br />
        <div>
          Showing {searchCount} results <br /> ({searchTime} seconds)
        </div>
        <br />
        <JSPopup
          trigger={<Link>⚠️ Important Notice ⚠️</Link>}
          position="top center"
        >
          <div>
            Downloading results with more than 10,000 fires on the map at a time can cause
            poor browser performance.
            <br />
            For the best experience, filter your search to be as detailed as
            possible.
          </div>
        </JSPopup>
        <br />
        <br />
        <Button variant="contained" onClick={handleDownloadCSV}>
          Download CSV Subset
        </Button>
        <img alt="[LOGO]" className="sdpLogoLeft" src={logo} />
      </div>
      <MapContainer
        style={{
          // width: "85vw",
          // margin: "auto",
          // float: "right",
          position: "relative",
          top: 0,
          left: 0,
        }}
        center={[39, -98]}
        zoom={4.5}
        zoomSnap={0.5}
        scrollWheelZoom={true}
      >
        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
        />
        {viewType == "points" &&
          results.map((fire) => (
            <Circle
              center={[fire.LATITUDE, fire.LONGITUDE]}
              key={fire.FOD_ID}
              color={"#ed2626"}
              radius={acresToMetersRadius(fire.FIRE_SIZE)}
            >
              <Popup>
                FOD ID: {fire.FOD_ID}
                <br />
                FPA ID: {fire.FPA_ID}
                <br />
                FIRE NAME: {fire.FIRE_NAME}
                <br />
                SIZE: {fire.FIRE_SIZE}
                <br />
                DATE: {fire.DISCOVERY_DATE}
                <br />
                LOCATION: {fire.LATITUDE}, {fire.LONGITUDE}
                <br />
                CAUSE: {fire.NWCG_CAUSE_CLASSIFICATION}
                <br />
                <Button
                  onClick={() => {
                    getFireDetails(fire.FOD_ID);
                    setModalVisible(true);
                  }}
                >
                  Additional Details
                </Button>
                <Modal
                  open={modalVisible}
                  onClose={handleClose}
                  aria-labelledby="modal-modal-title"
                  aria-describedby="modal-modal-description"
                  sx={{
                    overflow: "scroll",
                    margin: "auto",
                  }}
                >
                  <Box sx={modalStyle}>
                    <Typography
                      id="modal-modal-title"
                      variant="h6"
                      component="h2"
                    >
                      Additional Details for fire: {modalData.FOD_ID}
                    </Typography>
                    <Button
                      onClick={() => {
                        window
                          .open(
                            "https://docs.google.com/spreadsheets/d/1Or4V3SxyUu4vsBbMkop66Dt7Rzq4_UDv/edit?usp=sharing&ouid=108049105554866139180&rtpof=true&sd=true",
                            "_blank"
                          )
                          .focus();
                      }}
                    >
                      About our variables
                    </Button>
                    <Typography
                      id="modal-modal-description"
                      sx={{
                        maxHeight: 700,
                        overflow: "scroll",
                        mt: 2,
                        padding: "auto",
                      }}
                    >
                      {
                        Object.entries(modalData).map((key, val) => {
                          if(selectedFields.indexOf(key[0])>=0 || selectedFields.length==0){

                          if (key[1] === "") {
                            return (
                              <li>
                                {key[0]}: NaN
                              </li>
                            );
                          }
                          if (key[0] === "GACC_NIMO_Teams" || key[0] == "GACC_Area_Command_Teams" && key[1] == 0) {
                            return (
                              <li>
                                {key[0]}: Null
                              </li>
                            )
                          }


                            if (key[1] === 1) {
                              return (
                                <li>
                                  {key[0]}: 1
                                </li>
                              );
                            } else if (key[1] === 0.0) {
                              return (
                                <li>
                                  {key[0]}: 0
                                </li>
                              );
                            } else {
                              return (
                                <li>
                                  {key[0]}: {String(key[1])}
                                </li>
                              );
                            }
                          }
                        })
                      }
                    </Typography>
                  </Box>
                </Modal>
              </Popup>
            </Circle>
          ))}
        {viewType == "heatmap" && (
          <HeatmapLayer
            //our intensity is fire size which can be far larger than default of 30 i think
            max={Number.MAX_SAFE_INTEGER}
            // mess with radius for how detailed / full the heatmap will look
            radius={25}
            // this makes sure you always see more detail as you zoom
            useLocalExtrema
            fitBoundsOnUpdate
            points={results}
            longitudeExtractor={(point) => point.LONGITUDE}
            latitudeExtractor={(point) => point.LATITUDE}
            intensityExtractor={(point) => parseFloat(point.FIRE_SIZE)}
          />
        )}
      </MapContainer>
    </div>
  );
};

export default Data;
