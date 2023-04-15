import React from "react";
import logo from "./../components/sdp_logo_fire.png";
import diagram from "./../components/fires-wild-diagram.png";
import "./../styles.css";
import { Typography, Stack, Card } from '@mui/material';
import { Link, useMatch, useResolvedPath } from "react-router-dom";
import {roboto} from '@fontsource/roboto';

export default function About() {
  return (
      <div>
      <Stack spacing={2} >
      <Card sx={{width:'100vw',
                alignSelf: 'center',
                alignContent: 'center',
                textalign: 'center',
                bgcolor: '#cfe8fc',
                boxShadow: "8px 16px 80px -25px rgba(0,150,200,.5)",
      }}>
      <Typography variant='h2' sx={{fontFamily:'roboto'}}>
        <br></br>
        2F+ Mapper(v 1.5.0)
        <br></br>
        Interactive Visualization Portal for FPA-FOD-Attributes Dataset
        <br></br>
      </Typography>
      </Card>
      <Card sx={{width:'85vw',
                alignSelf: 'center',
                alignContent: 'left',
                textalign: 'left',
                bgcolor: '#cfe8fc',
                boxShadow: "0 8px 40px -12px rgba(0,0,0,0.3)",
                "&:hover": {
                  boxShadow: "0 16px 70px -12.125px rgba(0,0,0,0.3)"
                }
      }}>
      <Typography sx={{fontSize: 18, fontFamily: 'roboto'}}><b>Brief</b>
      <br></br>
      2F+ mapper interactively visualizes individual fire incidents from 1992-2020 
      and their attributes – including location, date, size, and cause, as well as social, 
      biophysical and biological characteristics – from the FPA-FOD-Attributes dataset. 
      FPA-FOD-Attributes was developed by Mr. Yavar Pourmohamad (PhD Student at Boise State), 
      and was supported by the Joint Fire Science Program (JFSP) grant number L21AC10247. 
      2F+ mapper portal was developed through two Boise State Computer Science senior design 
      projects by the “Fires Wild” and “Wildfire Wizards” teams (info below), under supervision 
      of Dr. Eric Henderson. Description of the wildfire attributes and their sources can be found&nbsp;
      <a href='https://docs.google.com/spreadsheets/d/1vJO7VtQnWXtx43itqYzdjvY_Qi3csCIM/edit#gid=528795580'>here</a>. 
      <br></br>
      <br></br>
      <b>Fires Wild Members:</b> David Adams; Benjamin Collins; Brenden Marks; Jeremy Stocking; Samuel Wasko (CS 481 - Fall 2022) 
      <br></br>
      <br></br>
      <b>Wildfire Wizards Members:</b> Ethan Raygor; Parker Balbach; Sawyer Ball (CS 481 - Spring 2023)
      <br></br>
      <br></br>
      <b>JFSP project investigators:</b> Dr. Mojtaba Sadegh (mojtabasadegh@boisestate.edu; Boise State University); Dr. John Abatzoglou (jabatzoglou@ucmerced.edu; University of California, Merced)
      <br></br>
      <br></br>
      <b>JFSP project collaborators:</b> Dr. Erica Fleishman (Oregon State University), Dr. Karen Short, Dr. Erin Belval, 
      and Dr. Matt Reeves (US Forest Service Rocky Mountain Research Station), Dr. Nick Nauslar (Bureau of Land Management), 
      Dr. Phil Higuera (University of Montana), Robb Lankston (Lankston Consulting, LLC), Arash Modaresi Rad (Boise State University)
      <br></br>
      <br></br>
      <b>More information:</b> Wildfires are increasingly impacting social and environmental systems in the United States. 
      From 1992-2020, 84% of wildfires in the conterminous United States (CONUS) were ignited by humans. 
      The ability to mitigate the undesirable effects of wildfires increases as understanding of the social, physical, 
      and biological conditions that co-occurred with or caused these ignitions, and contributed to the fire size. To this end, 
      we developed FPA-FOD-Attributes, which augments the sixth version of the Fire Program Analysis Fire-Occurrence Database (FPA-FOD) 
      with more than 300 attributes that coincide with the date and location of each fire ignition in CONUS. FPA-FOD contains information on location, 
      jurisdiction, discovery time, cause, and final size for &gt;2.2 million wildfire ignitions from 1992-2020 in CONUS 
      (&gt;2.3 million in the United States). For each ignition, we added attributes to characterize coincident weather and national 
      fire danger indices. We also added attributes related to topography, road, vegetation, climate normals, management jurisdiction, 
      human population density, social vulnerability, and wildfire suppression difficulty. Furthermore, we added satellite-based vegetation 
      indices on the ignition date and 12 months prior to it to provide information on fuel availability. This publicly available, 
      rich dataset can be used to answer numerous questions about the covariates associated with human- and lightning-ignited wildfires, and with wildfire growth.

        {/* <br></br>
        2F+ Mapper is an interactive website created as a part of a
        collaborative wildfire research plan. Please see &nbsp;
        <a href="https://www.boisestate.edu/news/2022/09/13/boise-state-researchers-lend-expertise-to-collaborative-wildfire-research-plan/" target="_blank">
          this article
        </a>
        . The website provides a map that utilizes the FPA-FOD+ database that
        has been modified from the FPA-FOD data that includes over roughly 250
        attributes per wildfire. Dr. Mojtaba Sadegh & Yavar Pourmohamad have
        outsourced the implementation of the website to Fires Wild. Fires Wild
        is a team of computer scientists who, as well as Dr. Mojtaba Sadegh &
        Yavar Pourmohamad are from Boise State University. Dr. Eric Henderson
        has connected Dr. Mojtaba Sadegh & Yavar Pourmohamad with the team via a
        senior project in Computer Science in the fall of 2022. */}
        </Typography>
        </Card>
        <Card sx={{width:'85vw',
                alignSelf: 'center',
                alignContent: 'left',
                textalign: 'left',
                bgcolor: '#cfe8fc',
                boxShadow: "0 8px 40px -12px rgba(0,0,0,0.3)",
                "&:hover": {
                  boxShadow: "0 16px 70px -12.125px rgba(0,0,0,0.3)"
                }
        }}>
        <Typography sx={{fontSize: 18, fontFamily: 'roboto'}}><b>Utlities</b>
        <br></br>
        The site currently gives the user the option to select the year of fire,
        the state of fire, and the county within that state to produce a map
        that marks where each fire occured. Fires Wild has also implemented a
        heatmap (no pun intended) where the size of the fire is considered and
        mapped across the US. 
        </Typography>
        </Card>
        <Card sx={{width:'85vw',
                alignSelf: 'center',    
                alignContent: 'left',
                textalign: 'left',
                bgcolor: '#cfe8fc',
                boxShadow: "0 8px 40px -12px rgba(0,0,0,0.3)",
                "&:hover": {
                  boxShadow: "0 16px 70px -12.125px rgba(0,0,0,0.3)"
                }
        }}>
        <Typography sx={{fontSize: 18, fontFamily: 'roboto'}}><b>For future site administrators</b>
        <br></br>
        To see the initial project proposal and direction of this project, see the 
        Fires Wild Project Proposal below.
        To access our repository and see the changes and implementations we have 
        made, please visit Team Wildfire Wizards repository&nbsp;
        <a href="https://github.com/cs481-ekh/s23-wildfire-wizards" target ="_blank">here.</a>
        To view the previous team's work, visit their repository&nbsp;
        <a href="https://github.com/cs481-ekh/f22-fires-wild" target="_blank">here.</a>
        </Typography>
        </Card>
        </Stack>
        <br></br>
        <br></br>
        <br></br>
      <h4>
        Fires Wild Members:<br></br>
        David Adams<br></br>
        Benjamin Collins<br></br>
        Brenden Marks<br></br>
        Jeremy Stocking<br></br>
        Samuel Wasko<br></br>
        CS 481 - Fall 2022<br></br>
        Dr. Henderson
      </h4>
      <h4>
        Wildfire Wizards Members: <br></br>
        Ethan Raygor <br></br>
        Parker Balbach <br></br>
        Sawyer Ball <br></br>
        CS 481 - Spring 2023 <br></br>
        Dr. Henderson
      </h4>
      <h2>Fires Wild Project Proposal</h2>
      <div className="projectProposal">
        <div className="leftBody">
          <h2>
            <b>1 Introduction</b>
          </h2>
          <h3>
            <b>1.1 Problem and Project Statement</b>
          </h3>
          <p>
            Wildfires are increasingly impacting social and environmental
            systems in the United States. From 1992-2020, 84% of wildfires in
            the conterminous United States (CONUS) were ignited by humans.
            <br></br>
            <br></br>
            We have been supplied with a publicly-available dataset in which we
            hope to enrich. The purpose of this project is to create a
            public-facing and easy-to-use website which disseminates and
            displays the data contained in the FPA-FOD-Plus dataset, which
            contains data collected by the US Forest Service, which has been
            enriched with a variety of covariates, including weather and land
            surface information at the point and date of fire incidents,
            provided by the sponsor, Dr. Mojtaba Sadegh and Mr. Yavar
            Pourmohamad.
            <br></br>
            <br></br>
            We plan to display this data graphically and make the data
            easily/readily available for use. The end goal of this project is to
            answer numerous questions about the covariates associated with
            wildfires, along with their growth patterns.
            <br></br>
            <br></br>
            In the right hands, these datasets could play a very important role
            in how we as humans can minimize our impact on nature with respect
            to wildfires.
          </p>
          <h3>
            <b>1.2 Operational Environment</b>
          </h3>
          <p>
            The environment for this project will be Docker containers built
            within a Docker network. This allows the project to be deployed to
            any infrastructure capable of running Docker. The end goal is to
            deploy this container to the BSU data cloud, or another cloud / web
            server as requested by the sponsor.
          </p>
          <h3>
            <b>1.3 Functional Requirements</b>
          </h3>
          <p>
            ● Database<br></br>
            &ensp; ○ Translating the data from the sponsor (.csv or .sqlite)
            into a form useful for our form of SQL database<br></br>
            &ensp; ○ Procedures for updating the database to contain new records
            from the sponsor’s format to the format of the database<br></br>
            &ensp; ○ Data is accessible to the backend (This is intended to be
            read-only, unless the stretch goal to build an admin page is
            reached, then it will allow for updating data. There are no plans to
            produce an interface to delete data as part of this effort.)
            <br></br>
            <br></br>
            <br></br>● Frontend (Data Visualization + UI / UX)<br></br>
            &ensp; ○ (Note: general UI attributes are modeled after the Climate
            Mapper tool located at
            <a href="https://climatetoolbox.org/tool/Climate-Mapper" target="_blank">
              {" "}
              this site
            </a>
            , as the sponsor is familiar with this tool.)<br></br>
            &ensp; ○ Global map in center of screen, defaulting to a view
            showing the contiguous United States, along with some
            yet-to-be-decided default data view (heatmap, grouping of objects,
            etc.)<br></br>
            &ensp; ○ Sidebar on left of page, which contains accordion dropdowns
            of enumerated variables and ranges / possible values to filter
            search.<br></br>
            &emsp; ■ A dictionary of the variables and their definitions and
            descriptions presented alongside the variables as they are selected
            <br></br>
            &ensp; ○ When attributes are selected (or a “search” button is
            pressed), a request is sent to the web server for the data.<br></br>
            &ensp; ○ From the JSON objects returned from the rest server,
            objects (circles, pinpoints, or heatmap illustrations) should be
            rendered onto the map<br></br>
            &emsp; ■ Depending on specific context, objects can be clickable to
            view more information about the datapoint<br></br>
            &ensp; ○ A button to switch to chart view showing the variable over
            time<br></br>
            &emsp; ■ (Stretch Goal: add feature to chart variables in different
            ways rather than value over time)<br></br>
            &ensp; ○ A button to download the currently viewed data in csv form
            <br></br>
            &emsp; ■ This can also be a “display raw data” button which switches
            to a text box containing a csv representation of the current map /
            chart view, with an option to copy or “download as file”.<br></br>
            &ensp; ○ Stretch Goal: Django admin page to allow direct import of
            data as csv<br></br>
            &emsp; ■ (Note: The built-in Django admin utility will allow edits
            to database records out of the box, but importing csv or other large
            datasets will take development effort)<br></br>
            <br></br>
            <br></br>● Web Server<br></br>
            &ensp; ○ When a request from the client is received, access the
            relevant data from the database, querying only for the filters
            requested by the client, and transform the data received into a
            &nbsp;
            <a href="https://geojson.org/" target="_blank">geoJSON</a> objects
          </p>
          <h3>
            <b>1.4 Assumptions and Limitations</b>
          </h3>
          <p>
            ● Development for this web app will be “desktop first”. While a
            small-screen mobile version of the site is possible with chosen web
            frameworks and libraries, it will not be a major focus, and instead
            a “stretch goal”. This is mostly due to time constraints, but also
            because we expect nearly all users of this site to be on desktop,
            laptop, or tablet computers, and want to focus our development time
            on making the site work best for those users.<br></br>
            <br></br>
            <br></br>● The database will contain a large number of large
            entries, which will make search somewhat inefficient. This is not
            something that we can control, but we will do our best to mitigate
            by using efficient queries.<br></br>
            <br></br>
            <br></br>● This project has a time scope of only 10 weeks worth of
            project effort, which limits the amount of enhancements, in-depth
            user testing, and other items that would be addressed in a larger
            scope project.
          </p>
          <h3>
            <b>1.5 Deliverables</b>
          </h3>
          <p>
            ● Source Code for this entire project, including unit tests and
            docker configuration<br></br>
            <br></br>
            <br></br>● Documentation<br></br>
            &ensp; ○ Deployment steps to host the web server alongside the
            database<br></br>
            &ensp; ○ MIT License document<br></br>
            &ensp; ○ Standard README with general information regarding the
            project and how to contribute, build, and deploy the project
            <br></br>
            &ensp; ○ Procedures related to updating the database to contain new
            records from the sponsor’s format to the format of the database
            <br></br>
            &ensp; ○ Stretch Goal: Documentation for use of the admin page
            utility to add data<br></br>
          </p>
          <h2>
            <b>2 Specifications and Analysis</b>
          </h2>
          <h3>
            <b>2.1 Proposed Approach</b>
          </h3>
          <p>
            <b>Back End Approach</b>
            <br></br>
            The back end approach will be comprised of a MySQL database to
            utilize the data:<br></br>
            <br></br>
            <br></br>● We went with MySQL for a database. Data has been given to
            us in raw .CSV file form. We went with this mainly due to our
            experience with it and its ease of use for our purposes.<br></br>
            <br></br>
            <br></br>● MySQL will be communicating with a Django Web Server
            within a Docker container. We went with Django due to our
            familiarity with Python, the modern, high-level approach, and claims
            of quick turnaround. We feel it is a strong fit for our goals after
            research.<br></br>
            <br></br>
            <br></br>
            <b>Front End Approach</b>
            <br></br>
            The front end has decided to go with a React Native front end
            framework. The React app will import the “Leaflet” and
            “react-leaflet” components for{" "}
            <a href="https://nodejs.org/api/all.html" target="_blank">React.NodeJS</a>
            <br></br>
            <br></br>
            <br></br>● We went with React due to its ease of use and
            capabilities in communicating with our Django backend.<br></br>
            <br></br>
            <br></br>● Packages and dependencies for React app selected by using
            the "<a href="https://yarnpkg.com/" target="_blank">yarn</a>" package manager and
            its `create react-app` utility.<br></br>
            <br></br>
            <br></br>● We chose{" "}
            <a href="https://leafletjs.com/reference.html" target="_blank">Leaflet</a>{" "}
            JavaScript library due to its popularity alongside good
            Docs/support. Also, it’s free and requires no API key. Overall we
            decided it’ll be a great open-source mapping api for our purposes.
            <br></br>
            <br></br>
            <br></br>●{" "}
            <a href="https://react-leaflet.js.org/docs/start-introduction/" target="_blank">
              React-leaflet
            </a>{" "}
            leverages the ability to use leaflet layers as react components.
            This was chosen due to our familiarity with javascript.<br></br>
            <br></br>
            <br></br>● We also chose{" "}
            <a href="https://recharts.org/en-US/" target="_blank">Recharts</a> due for its
            simplicity for rendering graphs within React.<br></br>
            <b>Alternative Approaches</b>
            <br></br>
            <br></br>
            <br></br>● Backend<br></br>
            &ensp; ○ Django alternative - <a href="https://www.php.net/" target="_blank">
              PHP
            </a>{" "}
            & PHPMyAdmin- older web tool that we feel won’t give us as simple of
            development on the backend of this project.<br></br>
            <br></br>
            <br></br>● Front End<br></br>
            &ensp; ○ React alternative - <a href="https://vuejs.net" target="_blank">Vue</a>-
            not as easy to learn and work with at our level of experience
            <br></br>
            &ensp; ○ Leaflet alternative - OpenLayers - less plugins available,
            more memory needed, Leaflet is considered a “higher-level API”
            <br></br>
            &ensp; ○ React-Leaflet alternative - use class components and
            lifecycle hooks (code the components ourselves) see this how-to:
            &nbsp;
            <a href="https://medium.com/@cherniavskii/creating-leaflet-maps-in-react-apps-e2750372d6d6" target="_blank">
              Use Leaflet in React apps{" "}
            </a>
          </p>
        </div>
        <div className="rightBody">
          <h3>
            <b>2.2 Architectural Diagram</b>
          </h3>
          <img alt="[DIAGRAM]" className="diagram" src={diagram} />
          <p>
            ● Docker Network: Allows docker containers to interface securely.
            This means the web server can request data from the database without
            exposing the database to the open internet. It also allows public
            access to the web application <br></br>
            &ensp; ○ Database Container <br></br>
            &emsp; ■ MySQL Database: Here is where a SQL copy of the
            FPA-FOD-Plus data is kept. SQL allows the data to be searched
            efficiently, which is necessary for a web application. <br></br>
            &ensp; ○ Backend Container <br></br>
            &emsp; ■ Django Web Server: Django is a web framework that is
            designed for quick development of web applications with a similar
            structure as we have architected here. This web server accepts
            requests from end users, and serves pages for interaction. <br></br>
            &ensp; ○ Front End Container <br></br>
            &emsp; ■ ReactJS: This is the library used for building the user
            interface, including navigation. This diagram assumes server-side
            rendering, which is highly useful for large datasets, but it is
            possible that the project switches to client side rendering for
            other benefits. <br></br>
            &emsp; ■ Leaflet: Used to create interactive maps, which will be
            used to display the wildfire data in map view. <br></br>
            &emsp; ■ ReCharts: Used to create interactive charts, which will be
            used to display the wildfire data in chart view. <br></br>● User’s
            Browser<br></br>
            &ensp; ○ This is where the javascript and html, rendered from the
            server, will be executed and displayed as the user interface. The
            user’s browser will send and receive requests from the Front End
            Container which will serve data for the website to function.
            <br></br>
            &emsp; ■ (Note: not shown here is the possibility for admins to log
            into the django backend directly to work with the dataset)
          </p>
          <h2>
            <b>3 Statement of Work</b>
          </h2>
          <h3>
            <b>3.1 Related Work</b>
          </h3>
          <p>
            The sponsor, Dr. Mojtaba Sadegh, has kindly provided samples of
            similar work in a different sector, more generally based on climate
            mapping. These samples are as follows:<br></br>●{" "}
            <a href="https://climatetoolbox.org/tool/climate-mapper" target="_blank">
              Climate Toolbox
            </a>
            <br></br>● <a href="https://climateengine.com/" target="_blank">Climate Engine</a>
            <br></br>
            <br></br>
            <br></br>
            Additionally, the original unmodified FPA-FOD dataset hosted in a MS
            Access database can be turned into a map, as documented in:{" "}
            <br></br>
            <br></br>
            <br></br>●{" "}
            <a href="https://regclim.coas.oregonstate.edu/FireStarts/fpa-fod_RODBC_01.html" target="_blank">
              FPA-FOD Original
            </a>
            <br></br>
            There are government tools to map current wildfires, but in our view
            they are lacking and seem to simply be updated by humans and not
            data driven <br></br>
            <br></br>
            <br></br>●{" "}
            <a href="https://fsapps.nwcg.gov/" target="_blank">Active Fire Mapping Program</a>{" "}
            <br></br>
            <br></br>
            <br></br>
            Finally, there are third-party tools to do a similar live view of
            fires, but are not driven by historical data that has been enriched
            in the same way: <br></br>●{" "}
            <a href="https://www.esri.com/en-us/disaster-response/disasters/wildfires" target="_blank">
              Disaster Response Program
            </a>
            <br></br>
          </p>
          <h3>
            <b>3.2 Description of end products</b>
          </h3>
          <p>
            The end product is a public-facing interactive website with an
            interface that allows users to choose variables, and request
            wildfire data based on those variables. The response to the request
            by the website is either a map, a graph, or a text box containing
            comma separated values (csv) of the data, depending on which view
            the user has currently chosen.
          </p>
          <h3>
            <b>3.3 Risks and Contingencies</b>
          </h3>
          <p>
            ● Much of the architecture, chosen frameworks, libraries, and other
            technology we have chosen to utilize is new to most, if not all of
            the team members. Because of this, we expect that many currently
            unknown variables due to these technologies will present themselves
            over the course of working on this project.<br></br>
            <br></br>
            <br></br>● The development team is not owners of the data to build
            this project. This means that development needs a partial focus on
            working with the supplied data in order to ensure that it can be
            searched and utilized efficiently<br></br>
            <br></br>
            <br></br>● As with all projects that are time-limited, there is a
            risk that not all evaluation criteria listed will be completed by
            the final date of the project. Diligent effort by team members will
            be taken to properly prioritize tasks that any leftover work will be
            trivial, and that by the end of the project, all milestones are
            reached.
          </p>
          <h2>
            <b>4 Project Milestones and Evaluation Criteria</b>
          </h2>
          <p>
            Create a set (2-4) of key milestones that will be used to measure
            the progress and successful completion of the project. Each
            milestone should describe a general set of tasks that must be
            completed before the milestone is reached. Specify the date the
            milestone will be completed.
          </p>
          <p>
            ● Simple Docker project with a database connected to a web server,
            which serves pages to a web frontend<br></br>
            &ensp; ○ Date: Sprint 0<br></br>
            &ensp; ○ Evaluation Criteria:<br></br>
            &emsp; ■ Docker-Compose file that instantiates containers for the
            database and web server<br></br>
            &emsp; ■ Backend container can request data and receives a response
            <br></br>
            &emsp; ■ Simple page is shown to the user<br></br>
            <br></br>
            <br></br>● Data ready for production, backend with models and
            functions to initialize and use the data, frontend with UI for
            displaying data, linked to backend functions<br></br>
            &ensp; ○ Date: Sprint 1<br></br>
            &ensp; ○ Evaluation Criteria:<br></br>
            &emsp; ■ Documentation for importing data to the database container,
            validated by other developers as part of setting up their local
            environment<br></br>
            &emsp; ■ Model of database items created for use in the backend
            system, with functions that request the data and populate entities
            without errors<br></br>
            &emsp; ■ Front-end “homepage” with a map, variable selection, and
            sample view showing visualized data<br></br>
            <br></br>
            <br></br>● Potentially Shippable Product containing the map, graph,
            raw data, and variables UI, with all properly hooked up components
            <br></br>
            &ensp; ○ Date: Sprint 4<br></br>
            &ensp; ○ Evaluation Criteria:<br></br>
            &emsp; ■ All functional requirements met<br></br>
            &emsp; ■ Demo to sponsor for review (though we intend to demo at
            sprint 3)<br></br>
            <br></br>
            <br></br>● Containerized application tested and ready to deploy,
            presented to sponsor, addressed sponsor feedback, approved by
            sponsor (Final product)<br></br>
            &ensp; ○ Date: Sprint 5<br></br>
            &ensp; ○ Evaluation Criteria:<br></br>
            &emsp; ■ 80% code coverage on backend functions<br></br>
            &emsp; ■ All UI elements have passing cypress tests for their
            functionality<br></br>
            &emsp; ■ Sponsor feedback from demo has been addressed; including UI
            changes, bug fixes, and other minor tweaks
          </p>
          <h2>
            <b>5 Testing and Validation</b>
          </h2>
          <p>
            <a href="https://docs.cypress.io/) is an end-to-end testing framework that will allow us to write" target="_blank">
              Cypress
            </a>{" "}
            &nbsp; functional tests for any UI functionality and REST endpoints.
            Cypress tests are easily integrated into the code pipeline via
            GitHub actions and are executed upon any merge to the main branch of
            our project. A complete test plan includes verification of any/all
            basic front end functionality along with validating returned data
            from individual REST endpoints. We need to guarantee data is
            returned from our endpoints in expected format and that the various
            front end features are working properly. When achieved, our
            application is sufficiently tested end to end.
            <br></br>
            <br></br>
            Every effort on this project is also peer reviewed and manually
            tested before it is designated as “ready to deploy.”
          </p>
        </div>
      </div>
      <h2>Wildfire Wizards Project Proposal</h2>
      <div className="projectProposal">
        <div className="leftBody">
          <h2>
            <b>1 Introduction</b>
          </h2>
          <h3>
            <b>1.1 Problem and Project Statement</b>
          </h3>
          <p>
            Wildfires destroy a lot of land, animal habitats, homes, and leave 
            a mess behind that can take many many years to heal properly. 
            Historical data, provided by the government and augmented by our 
            sponsors, could be a key factor in being able to predict when and 
            where a wildfire could occur next. The previous development team 
            was able to create a strong user interface that can be used to 
            easily view this data.
            <br></br>
            <br></br>
            Our goal for our project is to make the overall experience better 
            in terms of performance, visualization, and user experience. Right 
            now, there are multiple locations where data isn’t displayed 
            correctly, a very obvious performance issue when there are too many 
            items pulled in the query, and other issues. Our goal is to have 
            these issues resolved.
          </p>
          <h3>
            <b>1.2 Operational Environment</b>
          </h3>
          <p>
            The previous development team created the product using a 
            container and currently has the website deployed to the BSU data 
            cloud. The project will continue to be developed in this 
            environment and by the end of the semester, if requested by the 
            sponsors, move to its own public domain.
            <br></br>
            <br></br>
            The frontend of this web app is currently designed to work well 
            on standard browsers on a desktop. The project will continue to 
            be implemented with this in mind. Compatibility with other 
            platforms is a stretch goal and will be implemented if time 
            permits.
          </p>
          <h3>
            <b>1.3a Functional Requirements</b>
          </h3>
          <p>
            ● UX<br></br>
            &ensp; ○ When a fire instance is clicked on, it will show name, 
            size, and cause first<br></br>
            &ensp; ○ When showing “Additional Details”, the variables will be 
            determined when a user is querying. There will be another option, 
            in the form of another button, to see all variables<br></br>
            &ensp; ○ When showing Additional Details, variable descriptions 
            will be available in the websites UI via tooltips<br></br>
            &ensp; ○ When showing additional details, true/false values will 
            display as 1/0<br></br>
            &ensp; ○ Stretch goal: The website will be mobile compatible<br></br>
            <br></br>
            <br></br>
            <br></br>
            ● Data<br></br>
            &ensp; ○ When a user downloads data, the data will be correct<br></br>
            &ensp; ○ When a user downloads data, they will be able to specify 
            which subset of variables or specific variables they would like 
            downloaded. These variables can be determined when the user chooses 
            to download the data via an extra menu<br></br>
            &ensp; ○ When a user is querying, all dropdown menus will only 
            display correct values<br></br>
            &ensp; ○ Stretch Goal: When a query returns there will be other 
            options to visualize it. The user will be able to pick two 
            variables that will be compared in graphical form<br></br>
          </p>
          <h3>
            <b>1.3b Nonfunctional Requirements</b>
          </h3>
          <p>
            ● Performance<br></br>
            &ensp; ○ The query time will be 10% better than its current 
            implementation<br></br>
            &ensp; ○ The software will handle a query with too many results, 
            instead of becoming unresponsive<br></br>
          </p>
          <h3>
            <b>1.4 Assumptions and Limitations</b>
          </h3>
          <p>
            The previous development team was able to deliver a deployable web 
            application last semester. We anticipate very few limitations and 
            plan on delivering a releasable portal at the end of the semester.
          </p>
          <h3>
            <b>1.5 Deliverables</b>
          </h3>
          <p>
            ● Source code for entire project including unit tests and docker 
            configuration<br></br>
            <br></br>
            ● Documentation including:<br></br>
            &ensp; ○ Steps for deployment of web server and database<br></br>
            &ensp; ○ License document<br></br>
            &ensp; ○ README with general information with information about 
            the project and future development<br></br>
          </p>
          <h2>
            <b>2 Specifications and Analysis</b>
          </h2>
          <h3>
            <b>2.1 Proposed Approach</b>
          </h3>
          <p>
            As a team, we decided that the best approach to this project would 
            be to split the workload into two main sections: user interface and 
            database performance. We will have various smaller tasks that can 
            be done at any point if needed but these will be prioritized the 
            lowest as our “stretch goals”
            <br></br>
            <br></br>
            We are first going to work on the user interface work because that 
            is what is most important to our sponsors. Once we get to a good 
            spot with these tasks, we can then move to working on database 
            performance. Another approach we could take is working on both at 
            the same time and just dividing the work up between all of us.
          </p>
        </div>
        <div className="rightBody">
        <h3>
            <b>2.2 Architectural Diagram</b>
          </h3>
          <img alt="[DIAGRAM]" className="diagram" src={diagram} />
          <p>
            This architectural diagram was provided by the last development 
            team as they are the ones that set the architectural structure of 
            this project.
          </p>
          <h2>
            <b>3 Statement of Work</b>
          </h2>
          <h3>
            <b>3.1 Related Work</b>
          </h3>
          <p>
            There are a few wildfire tracking websites (particularly 
            <a href="https://inciweb.nwcg.gov/" target="_blank">
              The Incident Information System
            </a> and 
            <a href="https://www.nytimes.com/interactive/2022/us/fire-tracker-maps.html" target="_blank">
              New York Times Fire Tracker
            </a>); however, these websites do not have wildfire data dating 
            before 2022. These dashboards look to be centered around tracking 
            wildfire in real-time, rather than historical data.
            <br></br>
            <br></br>
            These wildfire tracking websites lack the functionality to download 
            their respective tables used in tracking. Their options to filter 
            data are inadequate, as the user is unable to filter by specific 
            areas. Lastly, the data provided is fairly bare bones, as each 
            wildfire only provides four data points (Incident Type, When the 
            fire was updated to the map, The size of the wildfire, and how much 
            of the fire is contained). 
          </p>
          <h3>
            <b>3.2 Description of end products</b>
          </h3>
          <p>
            The wildfire website will be available on all browsers and possibly 
            mobile devices if stretch goals are reached. A user will be able to 
            filter data based on the variables provided on the left side of the 
            map. Once the user filters the page, data points will appear on the 
            map. The radius of each data point will indicate the size of the 
            wildfire. Clicking on a specific point will display basic 
            information to the user. The user will be able to click 
            “additional details” in order to view more in depth information 
            about the specific wildfire. A user will have the ability to 
            download the complete data set in csv format or download a subset 
            of the data based on the filters they apply to the map.
          </p>
          <h3>
            <b>3.3 Risks and Contingencies</b>
          </h3>
          <p>
            We do not anticipate experiencing any risk for this project. This 
            legacy project has already provided a framework to work with. 
            There is a possibility that some aspects of the project may take 
            longer than anticipated. In this case, team members will take 
            proper steps to prioritize features that the sponsor deems most 
            important. The team will make an attentive effort in order to 
            ensure that all milestones are completed. 
          </p>
          <h2>
            <b>4 Project Milestones and Evaluation Criteria</b>
          </h2>
          <p>
            Milestone 1: PSP<br></br>
            We are developing an already shippable product so we are defining 
            our first milestone as having all forms of data updated as well as 
            having data validation be complete. Our sponsor has stressed the 
            importance of this happening so it is our first priority. This will 
            be completed when we have updated the data in the project with what 
            our sponsor has provided, and have provided a complete test suite 
            to make sure queries and downloads are providing the correct 
            information.
            <br></br>
            <br></br>
            Milestone 2: MVP<br></br>
            We will have a minimum viable product when we have completed our 
            functional requirements listed in section 1.3. This includes all of 
            the UI fixes, improved search and download options, and performance 
            improvements.
          </p>
          <h2>
            <b>5 Testing and Validation</b>
          </h2>
          <p>
            The previous team used a Cypress test suite for functional tests of 
            the UI and REST endpoints. They chose Cypress because it integrates 
            easily with github actions. We will continue to use and improve 
            upon the test suite designed by the previous team with the 
            following ideas in mind. We need to guarantee that data returned by 
            a user querying or by a user using the download feature is accurate 
            and in the correct format. We also need to ensure that all frontend 
            functionality is working properly. We may also manually test simple 
            parts of the UI as needed. 
          </p>
        </div>
      </div>
      <Link to={"/"}>
        <img alt="[LOGO]" className="sdpLogoLeft" src={logo} />
      </Link>
      </div>
  );
}
