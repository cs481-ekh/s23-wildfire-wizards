

def categoryHelper(categories):
    rtVal = []
    for c in categories:
        for f in fields(c):
            rtVal.append(f)
    if len(categories)==0:
        for f in defaultFields():
            rtVal.append(f)
    return rtVal

def defaultFields():
    rtVal = ["FOD_ID", "FPA_ID", "FIRE_NAME", "FIRE_SIZE", "DISCOVERY_DATE", 
    "LATITUDE", "LONGITUDE", "NWCG_CAUSE_CLASSIFICATION"]
    rtVal.reverse()
    return rtVal

def addAllCategories():
    rtVal = ["FPA_FOD",  
    "Annual Climate", "Cheat Grass", "Climate Normals", "GRIDMET", 
    "Climate Percentiles", "Ecoregions", "Topography", "Vegetation",
    "Risk Management Assistance", "Fire Regime Groups", "Fire Stations", 
    "Geographic Area Coordination Centers", "Gap Analysis Project", 
    "Gross Domestic Product", "Global Human Modification", "MODIS NDVI", 
    "NOAA NDVI", "National Land Cover Database", "National Preperdness Level", "Population", "Pyrome", "Road", 
    "Social Vulnerability Index", "Rangeland Production Monitoring Service",
    "Climate and Economic Justice Screening Tool"]
    return rtVal

def get_counties(state):
    state.upper()
    state_counties = {
        'ALABAMA': ['Autauga', 'Baldwin', 'Barbour', 'Bibb', 'Blount', 'Bullock', 'Butler', 'Calhoun', 'Chambers', 'Cherokee', 'Chilton', 'Choctaw', 'Clarke', 'Clay', 'Cleburne', 'Coffee', 'Colbert', 'Conecuh', 'Coosa', 'Covington', 'Crenshaw', 'Cullman', 'Dale', 'Dallas', 'DeKalb', 'Elmore', 'Escambia', 'Etowah', 'Fayette', 'Franklin', 'Geneva', 'Greene', 'Hale', 'Henry', 'Houston', 'Jackson', 'Jefferson', 'Lamar', 'Lauderdale', 'Lawrence', 'Lee', 'Limestone', 'Lowndes', 'Macon', 'Madison', 'Marengo', 'Marion', 'Marshall', 'Mobile', 'Monroe', 'Montgomery', 'Morgan', 'Perry', 'Pickens', 'Pike', 'Randolph', 'Russell', 'St. Clair', 'Shelby', 'Sumter', 'Talladega', 'Tallapoosa', 'Tuscaloosa', 'Walker', 'Washington', 'Wilcox', 'Winston'],
        'ALASKA': ['Aleutians East', 'Aleutians West', 'Anchorage', 'Bethel', 'Bristol Bay', 'Denali', 'Dillingham', 'Fairbanks North Star', 'Haines', 'Hoonah-Angoon', 'Juneau', 'Kenai Peninsula', 'Ketchikan Gateway', 'Kodiak Island', 'Lake and Peninsula', 'Matanuska-Susitna', 'Nome', 'North Slope', 'Northwest Arctic', 'Petersburg', 'Prince of Wales-Hyder', 'Sitka', 'Skagway', 'Southeast Fairbanks', 'Valdez-Cordova', 'Wrangell', 'Yakutat', 'Yukon-Koyukuk'],
        'ARIZONA': ['Apache', 'Cochise', 'Coconino', 'Gila', 'Graham', 'Greenlee', 'La Paz', 'Maricopa', 'Mohave', 'Navajo', 'Pima', 'Pinal', 'Santa Cruz', 'Yavapai', 'Yuma'],
        'ARKANSAS': ['Arkansas', 'Ashley', 'Baxter', 'Benton', 'Boone', 'Bradley', 'Calhoun', 'Carroll', 'Chicot', 'Clark', 'Clay', 'Cleburne', 'Cleveland', 'Columbia', 'Conway', 'Craighead', 'Crawford', 'Crittenden', 'Cross', 'Dallas', 'Desha', 'Drew', 'Faulkner', 'Franklin', 'Fulton', 'Garland', 'Grant', 'Greene', 'Hempstead', 'Hot Spring', 'Howard', 'Independence', 'Izard', 'Jackson', 'Jefferson', 'Johnson', 'Lafayette', 'Lawrence', 'Lee', 'Lincoln', 'Little River', 'Logan', 'Lonoke', 'Madison', 'Marion', 'Miller', 'Mississippi', 'Monroe', 'Montgomery', 'Nevada', 'Newton', 'Ouachita', 'Perry', 'Phillips', 'Pike', 'Poinsett', 'Polk', 'Pope', 'Prairie', 'Pulaski', 'Randolph', 'St. Francis', 'Saline', 'Scott', 'Searcy', 'Sebastian', 'Sevier', 'Sharp', 'Stone', 'Union', 'Van Buren', 'Washington', 'White', 'Woodruff', 'Yell'],
        'CALIFORNIA': ['Alameda', 'Alpine', 'Amador', 'Butte', 'Calaveras', 'Colusa', 'Contra Costa', 'Del Norte', 'El Dorado', 'Fresno', 'Glenn', 'Humboldt', 'Imperial', 'Inyo', 'Kern', 'Kings', 'Lake', 'Lassen', 'Los Angeles', 'Madera', 'Marin', 'Mariposa', 'Mendocino', 'Merced', 'Modoc', 'Mono', 'Monterey', 'Napa', 'Nevada', 'Orange', 'Placer', 'Plumas', 'Riverside', 'Sacramento', 'San Benito', 'San Bernardino', 'San Diego', 'San Francisco', 'San Joaquin', 'San Luis Obispo', 'San Mateo', 'Santa Barbara', 'Santa Clara', 'Santa Cruz', 'Shasta', 'Sierra', 'Siskiyou', 'Solano', 'Sonoma', 'Stanislaus', 'Sutter', 'Tehama', 'Trinity', 'Tulare', 'Tuolumne', 'Ventura', 'Yolo', 'Yuba'],
        'COLORADO': ['Adams', 'Alamosa', 'Arapahoe', 'Archuleta', 'Baca', 'Bent', 'Boulder', 'Broomfield', 'Chaffee', 'Cheyenne', 'Clear Creek', 'Conejos', 'Costilla', 'Crowley', 'Custer', 'Delta', 'Denver', 'Dolores', 'Douglas', 'Eagle', 'Elbert', 'El Paso', 'Fremont', 'Garfield', 'Gilpin', 'Grand', 'Gunnison', 'Hinsdale', 'Huerfano', 'Jackson', 'Jefferson', 'Kiowa', 'Kit Carson', 'Lake', 'La Plata', 'Larimer', 'Las Animas', 'Lincoln', 'Logan', 'Mesa', 'Mineral', 'Moffat', 'Montezuma', 'Montrose', 'Morgan', 'Otero', 'Ouray', 'Park', 'Phillips', 'Pitkin', 'Prowers', 'Pueblo', 'Rio Blanco', 'Rio Grande', 'Routt', 'Saguache', 'San Juan', 'San Miguel', 'Sedgwick', 'Summit', 'Teller', 'Washington', 'Weld', 'Yuma'],
        'CONNECTICUT': ['Fairfield', 'Hartford', 'Litchfield', 'Middlesex', 'New Haven', 'New London', 'Tolland', 'Windham'],
        'DISTRICT OF COLUMBIA': ['District of Columbia'],
        'DELAWARE': ['Kent', 'New Castle', 'Sussex'],
        'FLORIDA': ['Alachua', 'Baker', 'Bay', 'Bradford', 'Brevard', 'Broward', 'Calhoun', 'Charlotte', 'Citrus', 'Clay', 'Collier', 'Columbia', 'DeSoto', 'Dixie', 'Duval', 'Escambia', 'Flagler', 'Franklin', 'Gadsden', 'Gilchrist', 'Glades', 'Gulf', 'Hamilton', 'Hardee', 'Hendry', 'Hernando', 'Highlands', 'Hillsborough', 'Holmes', 'Indian River', 'Jackson', 'Jefferson', 'Lafayette', 'Lake', 'Lee', 'Leon', 'Levy', 'Liberty', 'Madison', 'Manatee', 'Marion', 'Martin', 'Miami-Dade', 'Monroe', 'Nassau', 'Okaloosa', 'Okeechobee', 'Orange', 'Osceola', 'Palm Beach', 'Pasco', 'Pinellas', 'Polk', 'Putnam', 'Santa Rosa', 'Sarasota', 'Seminole', 'St. Johns', 'St. Lucie', 'Sumter', 'Suwannee', 'Taylor', 'Union', 'Volusia', 'Wakulla', 'Walton', 'Washington'],
        'GEORGIA': ['Appling', 'Atkinson', 'Bacon', 'Baker', 'Baldwin', 'Banks', 'Barrow', 'Bartow', 'Ben Hill', 'Berrien', 'Bibb', 'Bleckley', 'Brantley', 'Brooks', 'Bryan', 'Bulloch', 'Burke', 'Butts', 'Calhoun', 'Camden', 'Candler', 'Carroll', 'Catoosa', 'Charlton', 'Chatham', 'Chattahoochee', 'Chattooga', 'Cherokee', 'Clarke', 'Clay', 'Clayton', 'Clinch', 'Cobb', 'Coffee', 'Colquitt', 'Columbia', 'Cook', 'Coweta', 'Crawford', 'Crisp', 'Dade', 'Dawson', 'Decatur', 'DeKalb', 'Dodge', 'Dooly', 'Dougherty', 'Douglas', 'Early', 'Echols', 'Effingham', 'Elbert', 'Emanuel', 'Evans', 'Fannin', 'Fayette', 'Floyd', 'Forsyth', 'Franklin', 'Fulton', 'Gilmer', 'Glascock', 'Glynn', 'Gordon', 'Grady', 'Greene', 'Gwinnett', 'Habersham', 'Hall', 'Hancock', 'Haralson', 'Harris', 'Hart', 'Heard', 'Henry', 'Houston', 'Irwin', 'Jackson', 'Jasper', 'Jeff Davis', 'Jefferson', 'Jenkins', 'Johnson', 'Jones', 'Lamar', 'Lanier', 'Laurens', 'Lee', 'Liberty', 'Lincoln', 'Long', 'Lowndes', 'Lumpkin', 'Macon', 'Madison', 'Marion', 'McDuffie', 'McIntosh', 'Meriwether', 'Miller', 'Mitchell', 'Monroe', 'Montgomery', 'Morgan', 'Murray', 'Muscogee', 'Newton', 'Oconee', 'Oglethorpe', 'Paulding', 'Peach', 'Pickens', 'Pierce', 'Pike', 'Polk', 'Pulaski', 'Putnam', 'Quitman', 'Rabun', 'Randolph', 'Richmond', 'Rockdale', 'Schley', 'Screven', 'Seminole', 'Spalding', 'Stephens', 'Stewart', 'Sumter', 'Talbot', 'Taliaferro', 'Tattnall', 'Taylor', 'Telfair', 'Terrell', 'Thomas', 'Tift', 'Toombs', 'Towns', 'Treutlen', 'Troup', 'Turner', 'Twiggs', 'Union', 'Upson', 'Walker', 'Walton', 'Ware', 'Warren', 'Washington', 'Wayne', 'Webster', 'Wheeler', 'White', 'Whitfield', 'Wilcox', 'Wilkes', 'Wilkinson', 'Worth'],
        'HAWAII': ['Hawaii', 'Honolulu', 'Kalawao', 'Kauai', 'Maui'],
        'IOWA': ['Adair', 'Adams', 'Allamakee', 'Appanoose', 'Audubon', 'Benton', 'Black Hawk', 'Boone', 'Bremer', 'Buchanan', 'Buena Vista', 'Butler', 'Calhoun', 'Carroll', 'Cass', 'Cedar', 'Cerro Gordo', 'Cherokee', 'Chickasaw', 'Clarke', 'Clay', 'Clayton', 'Clinton', 'Crawford', 'Dallas', 'Davis', 'Decatur', 'Delaware', 'Des Moines', 'Dickinson', 'Dubuque', 'Emmet', 'Fayette', 'Floyd', 'Franklin', 'Fremont', 'Greene', 'Grundy', 'Guthrie', 'Hamilton', 'Hancock', 'Hardin', 'Harrison', 'Henry', 'Howard', 'Humboldt', 'Ida', 'Iowa', 'Jackson', 'Jasper', 'Jefferson', 'Johnson', 'Jones', 'Keokuk', 'Kossuth', 'Lee', 'Linn', 'Louisa', 'Lucas', 'Lyon', 'Madison', 'Mahaska', 'Marion', 'Marshall', 'Mills', 'Mitchell', 'Monona', 'Monroe', 'Montgomery', 'Muscatine', 'O\'Brien', 'Osceola', 'Page', 'Palo Alto', 'Plymouth', 'Pocahontas', 'Polk', 'Pottawattamie', 'Poweshiek', 'Ringgold', 'Sac', 'Scott', 'Shelby', 'Sioux', 'Story', 'Tama', 'Taylor', 'Union', 'Van Buren', 'Wapello', 'Warren', 'Washington', 'Wayne', 'Webster', 'Winnebago', 'Winneshiek', 'Woodbury', 'Worth', 'Wright'],
        'IDAHO': ['Ada', 'Adams', 'Bannock', 'Bear Lake', 'Benewah', 'Bingham', 'Blaine', 'Boise', 'Bonner', 'Bonneville', 'Boundary', 'Butte', 'Camas', 'Canyon', 'Caribou', 'Cassia', 'Clark', 'Clearwater', 'Custer', 'Elmore', 'Franklin', 'Fremont', 'Gem', 'Gooding', 'Idaho', 'Jefferson', 'Jerome', 'Kootenai', 'Latah', 'Lemhi', 'Lewis', 'Lincoln', 'Madison', 'Minidoka', 'Nez Perce', 'Oneida', 'Owyhee', 'Payette', 'Power', 'Shoshone', 'Teton', 'Twin Falls', 'Valley', 'Washington'],
        'ILLINOIS': ['Adams', 'Alexander', 'Bond', 'Boone', 'Brown', 'Bureau', 'Calhoun', 'Carroll', 'Cass', 'Champaign', 'Christian', 'Clark', 'Clay', 'Clinton', 'Coles', 'Cook', 'Crawford', 'Cumberland', 'DeKalb', 'De Witt', 'Douglas', 'DuPage', 'Edgar', 'Edwards', 'Effingham', 'Fayette', 'Ford', 'Franklin', 'Fulton', 'Gallatin', 'Greene', 'Grundy', 'Hamilton', 'Hancock', 'Hardin', 'Henderson', 'Henry', 'Iroquois', 'Jackson', 'Jasper', 'Jefferson', 'Jersey', 'Jo Daviess', 'Johnson', 'Kane', 'Kankakee', 'Kendall', 'Knox', 'LaSalle', 'Lake', 'Lawrence', 'Lee', 'Livingston', 'Logan', 'McDonough', 'McHenry', 'McLean', 'Macon', 'Macoupin', 'Madison', 'Marion', 'Marshall', 'Mason', 'Massac', 'Menard', 'Mercer', 'Monroe', 'Montgomery', 'Morgan', 'Moultrie', 'Ogle', 'Peoria', 'Perry', 'Piatt', 'Pike', 'Pope', 'Pulaski', 'Putnam', 'Randolph', 'Richland', 'Rock Island', 'St. Clair', 'Saline', 'Sangamon', 'Schuyler', 'Scott', 'Shelby', 'Stark', 'Stephenson', 'Tazewell', 'Union', 'Vermilion', 'Wabash', 'Warren', 'Washington', 'Wayne', 'White', 'Whiteside', 'Will', 'Williamson', 'Winnebago', 'Woodford'],
        'INDIANA': ['Adams', 'Allen', 'Bartholomew', 'Benton', 'Blackford', 'Boone', 'Brown', 'Carroll', 'Cass', 'Clark', 'Clay', 'Clinton', 'Crawford', 'Daviess', 'Dearborn', 'Decatur', 'DeKalb', 'Delaware', 'Dubois', 'Elkhart', 'Fayette', 'Floyd', 'Fountain', 'Franklin', 'Fulton', 'Gibson', 'Grant', 'Greene', 'Hamilton', 'Hancock', 'Harrison', 'Hendricks', 'Henry', 'Howard', 'Huntington', 'Jackson', 'Jasper', 'Jay', 'Jefferson', 'Jennings', 'Johnson', 'Knox', 'Kosciusko', 'LaGrange', 'Lake', 'LaPorte', 'Lawrence', 'Madison', 'Marion', 'Marshall', 'Martin', 'Miami', 'Monroe', 'Montgomery', 'Morgan', 'Newton', 'Noble', 'Ohio', 'Orange', 'Owen', 'Parke', 'Perry', 'Pike', 'Porter', 'Posey', 'Pulaski', 'Putnam', 'Randolph', 'Ripley', 'Rush', 'St. Joseph', 'Scott', 'Shelby', 'Spencer', 'Starke', 'Steuben', 'Sullivan', 'Switzerland', 'Tippecanoe', 'Tipton', 'Union', 'Vanderburgh', 'Vermillion', 'Vigo', 'Wabash', 'Warren', 'Warrick', 'Washington', 'Wayne', 'Wells', 'White', 'Whitley'],
        'KANSAS': ['Allen', 'Anderson', 'Atchison', 'Barber', 'Barton', 'Bourbon', 'Brown', 'Butler', 'Chase', 'Chautauqua', 'Cherokee', 'Cheyenne', 'Clark', 'Clay', 'Cloud', 'Coffey', 'Comanche', 'Cowley', 'Crawford', 'Decatur', 'Dickinson', 'Doniphan', 'Douglas', 'Edwards', 'Elk', 'Ellis', 'Ellsworth', 'Finney', 'Ford', 'Franklin', 'Geary', 'Gove', 'Graham', 'Grant', 'Gray', 'Greeley', 'Greenwood', 'Hamilton', 'Harper', 'Harvey', 'Haskell', 'Hodgeman', 'Jackson', 'Jefferson', 'Jewell', 'Johnson', 'Kearny', 'Kingman', 'Kiowa', 'Labette', 'Lane', 'Leavenworth', 'Lincoln', 'Linn', 'Logan', 'Lyon', 'McPherson', 'Marion', 'Marshall', 'Meade', 'Miami', 'Mitchell', 'Montgomery', 'Morris', 'Morton', 'Nemaha', 'Neosho', 'Ness', 'Norton', 'Osage', 'Osborne', 'Ottawa', 'Pawnee', 'Phillips', 'Pottawatomie', 'Pratt', 'Rawlins', 'Reno', 'Republic', 'Rice', 'Riley', 'Rooks', 'Rush', 'Russell', 'Saline', 'Scott', 'Sedgwick', 'Seward', 'Shawnee', 'Sheridan', 'Sherman', 'Smith', 'Stafford', 'Stanton', 'Stevens', 'Sumner', 'Thomas', 'Trego', 'Wabaunsee', 'Wallace', 'Washington', 'Wichita', 'Wilson', 'Woodson', 'Wyandotte'],
        'KENTUCKY': ['Adair', 'Allen', 'Anderson', 'Ballard', 'Barren', 'Bath', 'Bell', 'Boone', 'Bourbon', 'Boyd', 'Boyle', 'Bracken', 'Breathitt', 'Breckinridge', 'Bullitt', 'Butler', 'Caldwell', 'Calloway', 'Campbell', 'Carlisle', 'Carroll', 'Carter', 'Casey', 'Christian', 'Clark', 'Clay', 'Clinton', 'Crittenden', 'Cumberland', 'Daviess', 'Edmonson', 'Elliott', 'Estill', 'Fayette', 'Fleming', 'Floyd', 'Franklin', 'Fulton', 'Gallatin', 'Garrard', 'Grant', 'Graves', 'Grayson', 'Green', 'Greenup', 'Hancock', 'Hardin', 'Harlan', 'Harrison', 'Hart', 'Henderson', 'Henry', 'Hickman', 'Hopkins', 'Jackson', 'Jefferson', 'Jessamine', 'Johnson', 'Kenton', 'Knott', 'Knox', 'Larue', 'Laurel', 'Lawrence', 'Lee', 'Leslie', 'Letcher', 'Lewis', 'Lincoln', 'Livingston', 'Logan', 'Lyon', 'Madison', 'Magoffin', 'Marion', 'Marshall', 'Martin', 'Mason', 'McCracken', 'McCreary', 'McLean', 'Meade', 'Menifee', 'Mercer', 'Metcalfe', 'Monroe', 'Montgomery', 'Morgan', 'Muhlenberg', 'Nelson', 'Nicholas', 'Ohio', 'Oldham', 'Owen', 'Owsley', 'Pendleton', 'Perry', 'Pike', 'Powell', 'Pulaski', 'Robertson', 'Rockcastle', 'Rowan', 'Russell', 'Scott', 'Shelby', 'Simpson', 'Spencer', 'Taylor', 'Todd', 'Trigg', 'Trimble', 'Union', 'Warren', 'Washington', 'Wayne', 'Webster', 'Whitley', 'Wolfe', 'Woodford'],
        'LOUISIANA': ['Acadia', 'Allen', 'Ascension', 'Assumption', 'Avoyelles', 'Beauregard', 'Bienville', 'Bossier', 'Caddo', 'Calcasieu', 'Caldwell', 'Cameron', 'Catahoula', 'Claiborne', 'Concordia', 'De Soto', 'East Baton Rouge', 'East Carroll', 'East Feliciana', 'Evangeline', 'Franklin', 'Grant', 'Iberia', 'Iberville', 'Jackson', 'Jefferson', 'Jefferson Davis', 'La Salle', 'Lafayette', 'Lafourche', 'Lincoln', 'Livingston', 'Madison', 'Morehouse', 'Natchitoches', 'Orleans', 'Ouachita', 'Plaquemines', 'Pointe Coupee', 'Rapides', 'Red River', 'Richland', 'Sabine', 'St. Bernard', 'St. Charles', 'St. Helena', 'St. James', 'St. John the Baptist', 'St. Landry', 'St. Martin', 'St. Mary', 'St. Tammany', 'Tangipahoa', 'Tensas', 'Terrebonne', 'Union', 'Vermilion', 'Vernon', 'Washington', 'Webster', 'West Baton Rouge', 'West Carroll', 'West Feliciana', 'Winn'],
        'MASSACHUSETTS': ['Barnstable', 'Berkshire', 'Bristol', 'Dukes', 'Essex', 'Franklin', 'Hampden', 'Hampshire', 'Middlesex', 'Nantucket', 'Norfolk', 'Plymouth', 'Suffolk', 'Worcester'],
        'MARYLAND': ['Allegany', 'Anne Arundel', 'Baltimore', 'Calvert', 'Caroline', 'Carroll', 'Cecil', 'Charles', 'Dorchester', 'Frederick', 'Garrett', 'Harford', 'Howard', 'Kent', 'Montgomery', 'Prince George\'s', "Queen Anne's", 'Somerset', 'St. Mary\'s', 'Talbot', 'Washington', 'Wicomico', 'Worcester'],
        'MAINE': ['Androscoggin', 'Aroostook', 'Cumberland', 'Franklin', 'Hancock', 'Kennebec', 'Knox', 'Lincoln', 'Oxford', 'Penobscot', 'Piscataquis', 'Sagadahoc', 'Somerset', 'Waldo', 'Washington', 'York'],
        'MICHIGAN': ['Alcona', 'Alger', 'Allegan', 'Alpena', 'Antrim', 'Arenac', 'Baraga', 'Barry', 'Bay', 'Benzie', 'Berrien', 'Branch', 'Calhoun', 'Cass', 'Charlevoix', 'Cheboygan', 'Chippewa', 'Clare', 'Clinton', 'Crawford', 'Delta', 'Dickinson', 'Eaton', 'Emmet', 'Genesee', 'Gladwin', 'Gogebic', 'Grand Traverse', 'Gratiot', 'Hillsdale', 'Houghton', 'Huron', 'Ingham', 'Ionia', 'Iosco', 'Iron', 'Isabella', 'Jackson', 'Kalamazoo', 'Kalkaska', 'Kent', 'Keweenaw', 'Lake', 'Lapeer', 'Leelanau', 'Lenawee', 'Livingston', 'Luce', 'Mackinac', 'Macomb', 'Manistee', 'Marquette', 'Mason', 'Mecosta', 'Menominee', 'Midland', 'Missaukee', 'Monroe', 'Montcalm', 'Montmorency', 'Muskegon', 'Newaygo', 'Oakland', 'Oceana', 'Ogemaw', 'Ontonagon', 'Osceola', 'Oscoda', 'Otsego', 'Ottawa', 'Presque Isle', 'Roscommon', 'Saginaw', 'St. Clair', 'St. Joseph', 'Sanilac', 'Schoolcraft', 'Shiawassee', 'Tuscola', 'Van Buren', 'Washtenaw', 'Wayne', 'Wexford'],
        'MINNESOTA': ['Aitkin', 'Anoka', 'Becker', 'Beltrami', 'Benton', 'Big Stone', 'Blue Earth', 'Brown', 'Carlton', 'Carver', 'Cass', 'Chippewa', 'Chisago', 'Clay', 'Clearwater', 'Cook', 'Cottonwood', 'Crow Wing', 'Dakota', 'Dodge', 'Douglas', 'Faribault', 'Fillmore', 'Freeborn', 'Goodhue', 'Grant', 'Hennepin', 'Houston', 'Hubbard', 'Isanti', 'Itasca', 'Jackson', 'Kanabec', 'Kandiyohi', 'Kittson', 'Koochiching', 'Lac qui Parle', 'Lake', 'Lake of the Woods', 'Le Sueur', 'Lincoln', 'Lyon', 'McLeod', 'Mahnomen', 'Marshall', 'Martin', 'Meeker', 'Mille Lacs', 'Morrison', 'Mower', 'Murray', 'Nicollet', 'Nobles', 'Norman', 'Olmsted', 'Otter Tail', 'Pennington', 'Pine', 'Pipestone', 'Polk', 'Pope', 'Ramsey', 'Red Lake', 'Redwood', 'Renville', 'Rice', 'Rock', 'Roseau', 'St. Louis', 'Scott', 'Sherburne', 'Sibley', 'Stearns', 'Steele', 'Stevens', 'Swift', 'Todd', 'Traverse', 'Wabasha', 'Wadena', 'Waseca', 'Washington', 'Watonwan', 'Wilkin', 'Winona', 'Wright', 'Yellow Medicine'],
        'MISSOURI': ['Adair', 'Andrew', 'Atchison', 'Audrain', 'Barry', 'Barton', 'Bates', 'Benton', 'Bollinger', 'Boone', 'Buchanan', 'Butler', 'Caldwell', 'Callaway', 'Camden', 'Cape Girardeau', 'Carroll', 'Carter', 'Cass', 'Cedar', 'Chariton', 'Christian', 'Clark', 'Clay', 'Clinton', 'Cole', 'Cooper', 'Crawford', 'Dade', 'Dallas', 'Daviess', 'DeKalb', 'Dent', 'Douglas', 'Dunklin', 'Franklin', 'Gasconade', 'Gentry', 'Greene', 'Grundy', 'Harrison', 'Henry', 'Hickory', 'Holt', 'Howard', 'Howell', 'Iron', 'Jackson', 'Jasper', 'Jefferson', 'Johnson', 'Knox', 'Laclede', 'Lafayette', 'Lawrence', 'Lewis', 'Lincoln', 'Linn', 'Livingston', 'McDonald', 'Macon', 'Madison', 'Maries', 'Marion', 'Mercer', 'Miller', 'Mississippi', 'Moniteau', 'Monroe', 'Montgomery', 'Morgan', 'New Madrid', 'Newton', 'Nodaway', 'Oregon', 'Osage', 'Ozark', 'Pemiscot', 'Perry', 'Pettis', 'Phelps', 'Pike', 'Platte', 'Polk', 'Pulaski', 'Putnam', 'Ralls', 'Randolph', 'Ray', 'Reynolds', 'Ripley', 'St. Charles', 'St. Clair', 'Ste. Genevieve', 'St. Francois', 'St. Louis', 'Saline', 'Schuyler', 'Scotland', 'Scott', 'Shannon', 'Shelby', 'Stoddard', 'Stone', 'Sullivan', 'Taney', 'Texas', 'Vernon', 'Warren', 'Washington', 'Wayne', 'Webster', 'Worth', 'Wright'],
        'MISSISSIPPI': ['Adams', 'Alcorn', 'Amite', 'Attala', 'Benton', 'Bolivar', 'Calhoun', 'Carroll', 'Chickasaw', 'Choctaw', 'Claiborne', 'Clarke', 'Clay', 'Coahoma', 'Copiah', 'Covington', 'DeSoto', 'Forrest', 'Franklin', 'George', 'Greene', 'Grenada', 'Hancock', 'Harrison', 'Hinds', 'Holmes', 'Humphreys', 'Issaquena', 'Itawamba', 'Jackson', 'Jasper', 'Jefferson', 'Jefferson Davis', 'Jones', 'Kemper', 'Lafayette', 'Lamar', 'Lauderdale', 'Lawrence', 'Leake', 'Lee', 'Leflore', 'Lincoln', 'Lowndes', 'Madison', 'Marion', 'Marshall', 'Monroe', 'Montgomery', 'Neshoba', 'Newton', 'Noxubee', 'Oktibbeha', 'Panola', 'Pearl River', 'Perry', 'Pike', 'Pontotoc', 'Prentiss', 'Quitman', 'Rankin', 'Scott', 'Sharkey', 'Simpson', 'Smith', 'Stone', 'Sunflower', 'Tallahatchie', 'Tate', 'Tippah', 'Tishomingo', 'Tunica', 'Union', 'Walthall', 'Warren', 'Washington', 'Wayne', 'Webster', 'Wilkinson', 'Winston', 'Yalobusha', 'Yazoo'],
        'MONTANA': ['Beaverhead', 'Big Horn', 'Blaine', 'Broadwater', 'Carbon', 'Carter', 'Cascade', 'Chouteau', 'Custer', 'Daniels', 'Dawson', 'Deer Lodge', 'Fallon', 'Fergus', 'Flathead', 'Gallatin', 'Garfield', 'Glacier', 'Golden Valley', 'Granite', 'Hill', 'Jefferson', 'Judith Basin', 'Lake', 'Lewis and Clark', 'Liberty', 'Lincoln', 'Madison', 'McCone', 'Meagher', 'Mineral', 'Missoula', 'Musselshell', 'Park', 'Petroleum', 'Phillips', 'Pondera', 'Powder River', 'Powell', 'Prairie', 'Ravalli', 'Richland', 'Roosevelt', 'Rosebud', 'Sanders', 'Sheridan', 'Silver Bow', 'Stillwater', 'Sweet Grass', 'Teton', 'Toole', 'Treasure', 'Valley', 'Wheatland', 'Wibaux', 'Yellowstone'],
        'NORTH CAROLINA': ['Alamance', 'Alexander', 'Alleghany', 'Anson', 'Ashe', 'Avery', 'Beaufort', 'Bertie', 'Bladen', 'Brunswick', 'Buncombe', 'Burke', 'Cabarrus', 'Caldwell', 'Camden', 'Carteret', 'Caswell', 'Catawba', 'Chatham', 'Cherokee', 'Chowan', 'Clay', 'Cleveland', 'Columbus', 'Craven', 'Cumberland', 'Currituck', 'Dare', 'Davidson', 'Davie', 'Duplin', 'Durham', 'Edgecombe', 'Forsyth', 'Franklin', 'Gaston', 'Gates', 'Graham', 'Granville', 'Greene', 'Guilford', 'Halifax', 'Harnett', 'Haywood', 'Henderson', 'Hertford', 'Hoke', 'Hyde', 'Iredell', 'Jackson', 'Johnston', 'Jones', 'Lee', 'Lenoir', 'Lincoln', 'McDowell', 'Macon', 'Madison', 'Martin', 'Mecklenburg', 'Mitchell', 'Montgomery', 'Moore', 'Nash', 'New Hanover', 'Northampton', 'Onslow', 'Orange', 'Pamlico', 'Pasquotank', 'Pender', 'Perquimans', 'Person', 'Pitt', 'Polk', 'Randolph', 'Richmond', 'Robeson', 'Rockingham', 'Rowan', 'Rutherford', 'Sampson', 'Scotland', 'Stanly', 'Stokes', 'Surry', 'Swain', 'Transylvania', 'Tyrrell', 'Union', 'Vance', 'Wake', 'Warren', 'Washington', 'Watauga', 'Wayne', 'Wilkes', 'Wilson', 'Yadkin', 'Yancey'],
        'NORTH DAKOTA': ['Adams', 'Barnes', 'Benson', 'Billings', 'Bottineau', 'Bowman', 'Burke', 'Burleigh', 'Cass', 'Cavalier', 'Dickey', 'Divide', 'Dunn', 'Eddy', 'Emmons', 'Foster', 'Golden Valley', 'Grand Forks', 'Grant', 'Griggs', 'Hettinger', 'Kidder', 'LaMoure', 'Logan', 'McHenry', 'McIntosh', 'McKenzie', 'McLean', 'Mercer', 'Morton', 'Mountrail', 'Nelson', 'Oliver', 'Pembina', 'Pierce', 'Ramsey', 'Ransom', 'Renville', 'Richland', 'Rolette', 'Sargent', 'Sheridan', 'Sioux', 'Slope', 'Stark', 'Steele', 'Stutsman', 'Towner', 'Traill', 'Walsh', 'Ward', 'Wells', 'Williams'],
        'NEBRASKA': ['Adams', 'Antelope', 'Arthur', 'Banner', 'Blaine', 'Boone', 'Box Butte', 'Boyd', 'Brown', 'Buffalo', 'Burt', 'Butler', 'Cass', 'Cedar', 'Chase', 'Cherry', 'Cheyenne', 'Clay', 'Colfax', 'Cuming', 'Custer', 'Dakota', 'Dawes', 'Dawson', 'Deuel', 'Dixon', 'Dodge', 'Douglas', 'Dundy', 'Fillmore', 'Franklin', 'Frontier', 'Furnas', 'Gage', 'Garden', 'Garfield', 'Gosper', 'Grant', 'Greeley', 'Hall', 'Hamilton', 'Harlan', 'Hayes', 'Hitchcock', 'Holt', 'Hooker', 'Howard', 'Jefferson', 'Johnson', 'Kearney', 'Keith', 'Keya Paha', 'Kimball', 'Knox', 'Lancaster', 'Lincoln', 'Logan', 'Loup', 'McPherson', 'Madison', 'Merrick', 'Morrill', 'Nance', 'Nemaha', 'Nuckolls', 'Otoe', 'Pawnee', 'Perkins', 'Phelps', 'Pierce', 'Platte', 'Polk', 'Red Willow', 'Richardson', 'Rock', 'Saline', 'Sarpy', 'Saunders', 'Scotts Bluff', 'Seward', 'Sheridan', 'Sherman', 'Sioux', 'Stanton', 'Thayer', 'Thomas', 'Thurston', 'Valley', 'Washington', 'Wayne', 'Webster', 'Wheeler', 'York'],
        'NEW HAMPSHIRE': ['Belknap', 'Carroll', 'Cheshire', 'Coos', 'Grafton', 'Hillsborough', 'Merrimack', 'Rockingham', 'Strafford', 'Sullivan'],
        'NEW JERSEY': ['Atlantic', 'Bergen', 'Burlington', 'Camden', 'Cape May', 'Cumberland', 'Essex', 'Gloucester', 'Hudson', 'Hunterdon', 'Mercer', 'Middlesex', 'Monmouth', 'Morris', 'Ocean', 'Passaic', 'Salem', 'Somerset', 'Sussex', 'Union', 'Warren'],
        'NEW MEXICO': ['Bernalillo', 'Catron', 'Chaves', 'Cibola', 'Colfax', 'Curry', 'De Baca', 'Dona Ana', 'Eddy', 'Grant', 'Guadalupe', 'Harding', 'Hidalgo', 'Lea', 'Lincoln', 'Los Alamos', 'Luna', 'McKinley', 'Mora', 'Otero', 'Quay', 'Rio Arriba', 'Roosevelt', 'Sandoval', 'San Juan', 'San Miguel', 'Santa Fe', 'Sierra', 'Socorro', 'Taos', 'Torrance', 'Union', 'Valencia'],
        'NEVADA': ['Carson City', 'Churchill', 'Clark', 'Douglas', 'Elko', 'Esmeralda', 'Eureka', 'Humboldt', 'Lander', 'Lincoln', 'Lyon', 'Mineral', 'Nye', 'Pershing', 'Storey', 'Washoe', 'White Pine'],
        'NEW YORK': ['Albany', 'Allegany', 'Bronx', 'Broome', 'Cattaraugus', 'Cayuga', 'Chautauqua', 'Chemung', 'Chenango', 'Clinton', 'Columbia', 'Cortland', 'Delaware', 'Dutchess', 'Erie', 'Essex', 'Franklin', 'Fulton', 'Genesee', 'Greene', 'Hamilton', 'Herkimer', 'Jefferson', 'Kings', 'Lewis', 'Livingston', 'Madison', 'Monroe', 'Montgomery', 'Nassau', 'New York', 'Niagara', 'Oneida', 'Onondaga', 'Ontario', 'Orange', 'Orleans', 'Oswego', 'Otsego', 'Putnam', 'Queens', 'Rensselaer', 'Richmond', 'Rockland', 'St. Lawrence', 'Saratoga', 'Schenectady', 'Schoharie', 'Schuyler', 'Seneca', 'Steuben', 'Suffolk', 'Sullivan', 'Tioga', 'Tompkins', 'Ulster', 'Warren', 'Washington', 'Wayne', 'Westchester', 'Wyoming', 'Yates'],
        'OHIO': ['Adams', 'Allen', 'Ashland', 'Ashtabula', 'Athens', 'Auglaize', 'Belmont', 'Brown', 'Butler', 'Carroll', 'Champaign', 'Clark', 'Clermont', 'Clinton', 'Columbiana', 'Coshocton', 'Crawford', 'Cuyahoga', 'Darke', 'Defiance', 'Delaware', 'Erie', 'Fairfield', 'Fayette', 'Franklin', 'Fulton', 'Gallia', 'Geauga', 'Greene', 'Guernsey', 'Hamilton', 'Hancock', 'Hardin', 'Harrison', 'Henry', 'Highland', 'Hocking', 'Holmes', 'Huron', 'Jackson', 'Jefferson', 'Knox', 'Lake', 'Lawrence', 'Licking', 'Logan', 'Lorain', 'Lucas', 'Madison', 'Mahoning', 'Marion', 'Medina', 'Meigs', 'Mercer', 'Miami', 'Monroe', 'Montgomery', 'Morgan', 'Morrow', 'Muskingum', 'Noble', 'Ottawa', 'Paulding', 'Perry', 'Pickaway', 'Pike', 'Portage', 'Preble', 'Putnam', 'Richland', 'Ross', 'Sandusky', 'Scioto', 'Seneca', 'Shelby', 'Stark', 'Summit', 'Trumbull', 'Tuscarawas', 'Union', 'Van Wert', 'Vinton', 'Warren', 'Washington', 'Wayne', 'Williams', 'Wood', 'Wyandot'],
        'OKLAHOMA': ['Adair', 'Alfalfa', 'Atoka', 'Beaver', 'Beckham', 'Blaine', 'Bryan', 'Caddo', 'Canadian', 'Carter', 'Cherokee', 'Choctaw', 'Cimarron', 'Cleveland', 'Coal', 'Comanche', 'Cotton', 'Craig', 'Creek', 'Custer', 'Delaware', 'Dewey', 'Ellis', 'Garfield', 'Garvin', 'Grady', 'Grant', 'Greer', 'Harmon', 'Harper', 'Haskell', 'Hughes', 'Jackson', 'Jefferson', 'Johnston', 'Kay', 'Kingfisher', 'Kiowa', 'Latimer', 'Le Flore', 'Lincoln', 'Logan', 'Love', 'Major', 'Marshall', 'Mayes', 'McClain', 'McCurtain', 'McIntosh', 'Murray', 'Muskogee', 'Noble', 'Nowata', 'Okfuskee', 'Oklahoma', 'Okmulgee', 'Osage', 'Ottawa', 'Pawnee', 'Payne', 'Pittsburg', 'Pontotoc', 'Pottawatomie', 'Pushmataha', 'Roger Mills', 'Rogers', 'Seminole', 'Sequoyah', 'Stephens', 'Texas', 'Tillman', 'Tulsa', 'Wagoner', 'Washington', 'Washita', 'Woods', 'Woodward'],
        'OREGON': ['Baker', 'Benton', 'Clackamas', 'Clatsop', 'Columbia', 'Coos', 'Crook', 'Curry', 'Deschutes', 'Douglas', 'Gilliam', 'Grant', 'Harney', 'Hood River', 'Jackson', 'Jefferson', 'Josephine', 'Klamath', 'Lake', 'Lane', 'Lincoln', 'Linn', 'Malheur', 'Marion', 'Morrow', 'Multnomah', 'Polk', 'Sherman', 'Tillamook', 'Umatilla', 'Union', 'Wallowa', 'Wasco', 'Washington', 'Wheeler', 'Yamhill'],
        'PENNSYLVANIA': ['Adams', 'Allegheny', 'Armstrong', 'Beaver', 'Bedford', 'Berks', 'Blair', 'Bradford', 'Bucks', 'Butler', 'Cambria', 'Cameron', 'Carbon', 'Centre', 'Chester', 'Clarion', 'Clearfield', 'Clinton', 'Columbia', 'Crawford', 'Cumberland', 'Dauphin', 'Delaware', 'Elk', 'Erie', 'Fayette', 'Forest', 'Franklin', 'Fulton', 'Greene', 'Huntingdon', 'Indiana', 'Jefferson', 'Juniata', 'Lackawanna', 'Lancaster', 'Lawrence', 'Lebanon', 'Lehigh', 'Luzerne', 'Lycoming', 'McKean', 'Mercer', 'Mifflin', 'Monroe', 'Montgomery', 'Montour', 'Northampton', 'Northumberland', 'Perry', 'Philadelphia', 'Pike', 'Potter', 'Schuylkill', 'Snyder', 'Somerset', 'Sullivan', 'Susquehanna', 'Tioga', 'Union', 'Venango', 'Warren', 'Washington', 'Wayne', 'Westmoreland', 'Wyoming', 'York'],
        'PUERTO RICO': ['Adjuntas', 'Aguada', 'Aguadilla', 'Aguas Buenas', 'Aibonito', 'Anasco', 'Arecibo', 'Arroyo', 'Barceloneta', 'Barranquitas', 'Bayamon', 'Cabo Rojo', 'Caguas', 'Camuy', 'Canovanas', 'Carolina', 'Catano', 'Cayey', 'Ceiba', 'Ciales', 'Cidra', 'Coamo', 'Comerio', 'Corozal', 'Culebra', 'Dorado', 'Fajardo', 'Florida', 'Guanica', 'Guayama', 'Guayanilla', 'Guaynabo', 'Gurabo', 'Hatillo', 'Hormigueros', 'Humacao', 'Isabela', 'Jayuya', 'Juana Diaz', 'Juncos', 'Lajas', 'Lares', 'Las Marias', 'Las Piedras', 'Loiza', 'Luquillo', 'Manati', 'Maricao', 'Maunabo', 'Mayaguez', 'Moca', 'Morovis', 'Naguabo', 'Naranjito', 'Orocovis', 'Patillas', 'Penuelas', 'Ponce', 'Quebradillas', 'Rincon', 'Rio Grande', 'Sabana Grande', 'Salinas', 'San German', 'San Juan', 'San Lorenzo', 'San Sebastian', 'Santa Isabel', 'Toa Alta', 'Toa Baja', 'Trujillo Alto', 'Utuado', 'Vega Alta', 'Vega Baja', 'Vieques', 'Villalba', 'Yabucoa', 'Yauco'],
        'RHODE ISLAND': ['Bristol', 'Kent', 'Newport', 'Providence', 'Washington'],
        'SOUTH CAROLINA': ['Abbeville', 'Aiken', 'Allendale', 'Anderson', 'Bamberg', 'Barnwell', 'Beaufort', 'Berkeley', 'Calhoun', 'Charleston', 'Cherokee', 'Chester', 'Chesterfield', 'Clarendon', 'Colleton', 'Darlington', 'Dillon', 'Dorchester', 'Edgefield', 'Fairfield', 'Florence', 'Georgetown', 'Greenville', 'Greenwood', 'Hampton', 'Horry', 'Jasper', 'Kershaw', 'Lancaster', 'Laurens', 'Lee', 'Lexington', 'Marion', 'Marlboro', 'McCormick', 'Newberry', 'Oconee', 'Orangeburg', 'Pickens', 'Richland', 'Saluda', 'Spartanburg', 'Sumter', 'Union', 'Williamsburg', 'York'],
        'SOUTH DAKOTA': ['Aurora', 'Beadle', 'Bennett', 'Bon Homme', 'Brookings', 'Brown', 'Brule', 'Buffalo', 'Butte', 'Campbell', 'Charles Mix', 'Clark', 'Clay', 'Codington', 'Corson', 'Custer', 'Davison', 'Day', 'Deuel', 'Dewey', 'Douglas', 'Edmunds', 'Fall River', 'Faulk', 'Grant', 'Gregory', 'Haakon', 'Hamlin', 'Hand', 'Hanson', 'Harding', 'Hughes', 'Hutchinson', 'Hyde', 'Jackson', 'Jerauld', 'Jones', 'Kingsbury', 'Lake', 'Lawrence', 'Lincoln', 'Lyman', 'McCook', 'McPherson', 'Marshall', 'Meade', 'Mellette', 'Miner', 'Minnehaha', 'Moody', 'Oglala Lakota', 'Pennington', 'Perkins', 'Potter', 'Roberts', 'Sanborn', 'Spink', 'Stanley', 'Sully', 'Todd', 'Tripp', 'Turner', 'Union', 'Walworth', 'Yankton', 'Ziebach'],
        'TENNESSEE': ['Anderson', 'Bedford', 'Benton', 'Bledsoe', 'Blount', 'Bradley', 'Campbell', 'Cannon', 'Carroll', 'Carter', 'Cheatham', 'Chester', 'Claiborne', 'Clay', 'Cocke', 'Coffee', 'Crockett', 'Cumberland', 'Davidson', 'Decatur', 'DeKalb', 'Dickson', 'Dyer', 'Fayette', 'Fentress', 'Franklin', 'Gibson', 'Giles', 'Grainger', 'Greene', 'Grundy', 'Hamblen', 'Hamilton', 'Hancock', 'Hardeman', 'Hardin', 'Hawkins', 'Haywood', 'Henderson', 'Henry', 'Hickman', 'Houston', 'Humphreys', 'Jackson', 'Jefferson', 'Johnson', 'Knox', 'Lake', 'Lauderdale', 'Lawrence', 'Lewis', 'Lincoln', 'Loudon', 'Macon', 'Madison', 'Marion', 'Marshall', 'Maury', 'McMinn', 'McNairy', 'Meigs', 'Monroe', 'Montgomery', 'Moore', 'Morgan', 'Obion', 'Overton', 'Perry', 'Pickett', 'Polk', 'Putnam', 'Rhea', 'Roane', 'Robertson', 'Rutherford', 'Scott', 'Sequatchie', 'Sevier', 'Shelby', 'Smith', 'Stewart', 'Sullivan', 'Sumner', 'Tipton', 'Trousdale', 'Unicoi', 'Union', 'Van Buren', 'Warren', 'Washington', 'Wayne', 'Weakley', 'White', 'Williamson', 'Wilson'],
        'TEXAS': ['Anderson', 'Andrews', 'Angelina', 'Aransas', 'Archer', 'Armstrong', 'Atascosa', 'Austin', 'Bailey', 'Bandera', 'Bastrop', 'Baylor', 'Bee', 'Bell', 'Bexar', 'Blanco', 'Borden', 'Bosque', 'Bowie', 'Brazoria', 'Brazos', 'Brewster', 'Briscoe', 'Brooks', 'Brown', 'Burleson', 'Burnet', 'Caldwell', 'Calhoun', 'Callahan', 'Cameron', 'Camp', 'Carson', 'Cass', 'Castro', 'Chambers', 'Cherokee', 'Childress', 'Clay', 'Cochran', 'Coke', 'Coleman', 'Collin', 'Collingsworth', 'Colorado', 'Comal', 'Comanche', 'Concho', 'Cooke', 'Coryell', 'Cottle', 'Crane', 'Crockett', 'Crosby', 'Culberson', 'Dallam', 'Dallas', 'Dawson', 'Deaf Smith', 'Delta', 'Denton', 'DeWitt', 'Dickens', 'Dimmit', 'Donley', 'Duval', 'Eastland', 'Ector', 'Edwards', 'Ellis', 'El Paso', 'Erath', 'Falls', 'Fannin', 'Fayette', 'Fisher', 'Floyd', 'Foard', 'Fort Bend', 'Franklin', 'Freestone', 'Frio', 'Gaines', 'Galveston', 'Garza', 'Gillespie', 'Glasscock', 'Goliad', 'Gonzales', 'Gray', 'Grayson', 'Gregg', 'Grimes', 'Guadalupe', 'Hale', 'Hall', 'Hamilton', 'Hansford', 'Hardeman', 'Hardin', 'Harris', 'Harrison', 'Hartley', 'Haskell', 'Hays', 'Hemphill', 'Henderson', 'Hidalgo', 'Hill', 'Hockley', 'Hood', 'Hopkins', 'Houston', 'Howard', 'Hudspeth', 'Hunt', 'Hutchinson', 'Irion', 'Jack', 'Jackson', 'Jasper', 'Jeff Davis', 'Jefferson', 'Jim Hogg', 'Jim Wells', 'Johnson', 'Jones', 'Karnes', 'Kaufman', 'Kendall', 'Kenedy', 'Kent', 'Kerr', 'Kimble', 'King', 'Kinney', 'Kleberg', 'Knox', 'Lamar', 'Lamb', 'Lampasas', 'La Salle', 'Lavaca', 'Lee', 'Leon', 'Liberty', 'Limestone', 'Lipscomb', 'Live Oak', 'Llano', 'Loving', 'Lubbock', 'Lynn', 'McCulloch', 'McLennan', 'McMullen', 'Madison', 'Marion', 'Martin', 'Mason', 'Matagorda', 'Maverick', 'Medina', 'Menard', 'Midland', 'Milam', 'Mills', 'Mitchell', 'Montague', 'Montgomery', 'Moore', 'Morris', 'Motley', 'Nacogdoches', 'Navarro', 'Newton', 'Nolan', 'Nueces', 'Ochiltree', 'Oldham', 'Orange', 'Palo Pinto', 'Panola', 'Parker', 'Parmer', 'Pecos', 'Polk', 'Potter', 'Presidio', 'Rains', 'Randall', 'Reagan', 'Real', 'Red River', 'Reeves', 'Refugio', 'Roberts', 'Robertson', 'Rockwall', 'Runnels', 'Rusk', 'Sabine', 'San Augustine', 'San Jacinto', 'San Patricio', 'San Saba', 'Schleicher', 'Scurry', 'Shackelford', 'Shelby', 'Sherman', 'Smith', 'Somervell', 'Starr', 'Stephens', 'Sterling', 'Stonewall', 'Sutton', 'Swisher', 'Tarrant', 'Taylor', 'Terrell', 'Terry', 'Throckmorton', 'Titus', 'Tom Green', 'Travis', 'Trinity', 'Tyler', 'Upshur', 'Upton', 'Uvalde', 'Val Verde', 'Van Zandt', 'Victoria', 'Walker', 'Waller', 'Ward', 'Washington', 'Webb', 'Wharton', 'Wheeler', 'Wichita', 'Wilbarger', 'Willacy', 'Williamson', 'Wilson', 'Winkler', 'Wise', 'Wood', 'Yoakum', 'Young', 'Zapata', 'Zavala'],
        'UTAH': ['Beaver', 'Box Elder', 'Cache', 'Carbon', 'Daggett', 'Davis', 'Duchesne', 'Emery', 'Garfield', 'Grand', 'Iron', 'Juab', 'Kane', 'Millard', 'Morgan', 'Piute', 'Rich', 'Salt Lake', 'San Juan', 'Sanpete', 'Sevier', 'Summit', 'Tooele', 'Uintah', 'Utah', 'Wasatch', 'Washington', 'Wayne', 'Weber'],
        'VIRGINIA': ['Accomack', 'Albemarle', 'Alleghany', 'Amelia', 'Amherst', 'Appomattox', 'Arlington', 'Augusta', 'Bath', 'Bedford', 'Bland', 'Botetourt', 'Brunswick', 'Buchanan', 'Buckingham', 'Campbell', 'Caroline', 'Carroll', 'Charles City', 'Charlotte', 'Chesterfield', 'Clarke', 'Craig', 'Culpeper', 'Cumberland', 'Dickenson', 'Dinwiddie', 'Essex', 'Fairfax', 'Fauquier', 'Floyd', 'Fluvanna', 'Franklin', 'Frederick', 'Giles', 'Gloucester', 'Goochland', 'Grayson', 'Greene', 'Greensville', 'Halifax', 'Hanover', 'Henrico', 'Henry', 'Highland', 'Isle of Wight', 'James City', 'King and Queen', 'King George', 'King William', 'Lancaster', 'Lee', 'Loudoun', 'Louisa', 'Lunenburg', 'Madison', 'Mathews', 'Mecklenburg', 'Middlesex', 'Montgomery', 'Nelson', 'New Kent', 'Northampton', 'Northumberland', 'Nottoway', 'Orange', 'Page', 'Patrick', 'Pittsylvania', 'Powhatan', 'Prince Edward', 'Prince George', 'Prince William', 'Pulaski', 'Rappahannock', 'Richmond', 'Roanoke', 'Rockbridge', 'Rockingham', 'Russell', 'Scott', 'Shenandoah', 'Smyth', 'Southampton', 'Spotsylvania', 'Stafford', 'Surry', 'Sussex', 'Tazewell', 'Warren', 'Washington', 'Westmoreland', 'Wise', 'Wythe', 'York'],
        'VERMONT': ['Addison', 'Bennington', 'Caledonia', 'Chittenden', 'Essex', 'Franklin', 'Grand Isle', 'Lamoille', 'Orange', 'Orleans', 'Rutland', 'Washington', 'Windham', 'Windsor'],
        'WASHINGTON': ['Adams', 'Asotin', 'Benton', 'Chelan', 'Clallam', 'Clark', 'Columbia', 'Cowlitz', 'Douglas', 'Ferry', 'Franklin', 'Garfield', 'Grant', 'Grays Harbor', 'Island', 'Jefferson', 'King', 'Kitsap', 'Kittitas', 'Klickitat', 'Lewis', 'Lincoln', 'Mason', 'Okanogan', 'Pacific', 'Pend Oreille', 'Pierce', 'San Juan', 'Skagit', 'Skamania', 'Snohomish', 'Spokane', 'Stevens', 'Thurston', 'Wahkiakum', 'Walla Walla', 'Whatcom', 'Whitman', 'Yakima'],
        'WISCONSIN': ['Adams', 'Ashland', 'Barron', 'Bayfield', 'Brown', 'Buffalo', 'Burnett', 'Calumet', 'Chippewa', 'Clark', 'Columbia', 'Crawford', 'Dane', 'Dodge', 'Door', 'Douglas', 'Dunn', 'Eau Claire', 'Florence', 'Fond du Lac', 'Forest', 'Grant', 'Green', 'Green Lake', 'Iowa', 'Iron', 'Jackson', 'Jefferson', 'Juneau', 'Kenosha', 'Kewaunee', 'La Crosse', 'Lafayette', 'Langlade', 'Lincoln', 'Manitowoc', 'Marathon', 'Marinette', 'Marquette', 'Menominee', 'Milwaukee', 'Monroe', 'Oconto', 'Oneida', 'Outagamie', 'Ozaukee', 'Pepin', 'Pierce', 'Polk', 'Portage', 'Price', 'Racine', 'Richland', 'Rock', 'Rusk', 'St. Croix', 'Sauk', 'Sawyer', 'Shawano', 'Sheboygan', 'Taylor', 'Trempealeau', 'Vernon', 'Vilas', 'Walworth', 'Washburn', 'Washington', 'Waukesha', 'Waupaca', 'Waushara', 'Winnebago', 'Wood'],
        'WEST VIRGINIA': ['Barbour', 'Berkeley', 'Boone', 'Braxton', 'Brooke', 'Cabell', 'Calhoun', 'Clay', 'Doddridge', 'Fayette', 'Gilmer', 'Grant', 'Greenbrier', 'Hampshire', 'Hancock', 'Hardy', 'Harrison', 'Jackson', 'Jefferson', 'Kanawha', 'Lewis', 'Lincoln', 'Logan', 'Marion', 'Marshall', 'Mason', 'McDowell', 'Mercer', 'Mineral', 'Mingo', 'Monongalia', 'Monroe', 'Morgan', 'Nicholas', 'Ohio', 'Pendleton', 'Pleasants', 'Pocahontas', 'Preston', 'Putnam', 'Raleigh', 'Randolph', 'Ritchie', 'Roane', 'Summers', 'Taylor', 'Tucker', 'Tyler', 'Upshur', 'Wayne', 'Webster', 'Wetzel', 'Wirt', 'Wood', 'Wyoming'],
        'WYOMING': ['Albany', 'Big Horn', 'Campbell', 'Carbon', 'Converse', 'Crook', 'Fremont', 'Goshen', 'Hot Springs', 'Johnson', 'Laramie', 'Lincoln', 'Natrona', 'Niobrara', 'Park', 'Platte', 'Sheridan', 'Sublette', 'Sweetwater', 'Teton', 'Uinta', 'Washakie', 'Weston']
    }
    return state_counties[state]

def postalToState(s):
    rtVal = ''
    if s=='AK':
        rtVal='Alaska'
    elif s=='AL':
        rtVal='Alabama'
    elif s=='AR':
        rtVal='Arkansas'
    elif s=='AZ':
        rtVal='Arizona'
    elif s=='CA': 
        rtVal='California'
    elif s=='CO': 
        rtVal='Colorado'
    elif s=='CT': 
        rtVal='Connecticut'
    elif s=='DC': 
        rtVal='District of Columbia'
    elif s=='DE':
        rtVal='Deleware'
    elif s=='FL':
        rtVal='Florida'
    elif s=='GA':
        rtVal='Georgia'
    elif s=='HI':
        rtVal='Hawaii'
    elif s=='IA':
        rtVal='Iowa'
    elif s=='ID':
        rtVal='Idaho'
    elif s=='IL':
        rtVal='Illinois'
    elif s=='IN':
        rtVal='Indiana'
    elif s=='KS':
        rtVal='Kansas'
    elif s=='KY':
        rtVal='Kentucky'
    elif s=='LA':
        rtVal='Louisiana'
    elif s=='MA':
        rtVal='Massachusetts'
    elif s=='MD':
        rtVal='Maryland'
    elif s=='ME':
        rtVal='Maine'
    elif s=='MI':
        rtVal='Michigan'
    elif s=='MN':
        rtVal='Minnesota'
    elif s=='MO':
        rtVal='Missouri'
    elif s=='MS':
        rtVal='Mississippi'
    elif s=='MT':
        rtVal='Montana'
    elif s=='NC':
        rtVal='North Carolina'
    elif s=='ND':
        rtVal='North Dakota'
    elif s=='NE':
        rtVal='Nebraska'
    elif s=='NH':
        rtVal='New Hampshire'
    elif s=='NJ':
        rtVal='New Jersey'
    elif s=='NM':
        rtVal='New Mexico'
    elif s=='NV':
        rtVal='Nevada'
    elif s=='NY':
        rtVal='New York'
    elif s=='OH':
        rtVal='Ohio'
    elif s=='OK': 
        rtVal='Oklahoma'
    elif s=='OR': 
        rtVal='Oregon'
    elif s=='PA': 
        rtVal='Pennsylvania'
    elif s=='PR': 
        rtVal='Puerto Rico'
    elif s=='RI': 
        rtVal='Rhode Island'
    elif s=='SC': 
        rtVal='South Carolina'
    elif s=='SD': 
        rtVal='South Dakota'
    elif s=='TN': 
        rtVal='Tennessee'
    elif s=='TX': 
        rtVal='Texas'
    elif s=='UT': 
        rtVal='Utah'
    elif s=='VA': 
        rtVal='Virginia'
    elif s=='VT':
        rtVal='Vermont'
    elif s=='WA': 
        rtVal='Washington'
    elif s=='WI': 
        rtVal='Wisconsin'
    elif s=='WV': 
        rtVal='West Virginia'
    elif s=='WY':
        rtVal='Wyoming'
    return rtVal

def stateList():
    rtVal = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 
    'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 
    'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 
    'OH', 'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 
    'VT','WA', 'WI', 'WV', 'WY']
    return rtVal

def fields(category):
    rtVal = []
    if category=='FPA_FOD' :
        rtVal.append('FOD_ID')
        rtVal.append('FPA_ID')
        rtVal.append('SOURCE_SYSTEM_TYPE')
        rtVal.append('SOURCE_SYSTEM')
        rtVal.append('NWCG_REPORTING_AGENCY')
        rtVal.append('NWCG_REPORTING_UNIT_ID')
        rtVal.append('SOURCE_REPORTING_UNIT')
        rtVal.append('SOURCE_REPORTING_UNIT_NAME')
        rtVal.append('LOCAL_FIRE_REPORT_ID')
        rtVal.append('LOCAL_INCIDENT_ID')
        rtVal.append('FIRE_CODE')
        rtVal.append('FIRE_NAME')
        rtVal.append('ICS_209_PLUS_INCIDENT_JOIN_ID')
        rtVal.append('ICS_209_PLUS_COMPLEX_JOIN_ID')
        rtVal.append('MTBS_ID')
        rtVal.append('MTBS_FIRE_NAME')
        rtVal.append('COMPLEX_NAME')
        rtVal.append('FIRE_YEAR')
        rtVal.append('DISCOVERY_DATE')
        rtVal.append('DISCOVERY_DOY')
        rtVal.append('DISCOVERY_TIME')
        rtVal.append('NWCG_CAUSE_CLASSIFICATION')
        rtVal.append('NWCG_GENERAL_CAUSE')
        rtVal.append('NWCG_CAUSE_AGE_CATEGORY')
        rtVal.append('CONT_DATE')
        rtVal.append('CONT_DOY')
        rtVal.append('CONT_TIME')
        rtVal.append('FIRE_SIZE')
        rtVal.append('FIRE_SIZE_CLASS')
        rtVal.append('LATITUDE')
        rtVal.append('LONGITUDE')
        rtVal.append('OWNER_DESCR')
        rtVal.append('STATE')
        rtVal.append('COUNTY')
        rtVal.append('FIPS_CODE')
        rtVal.append('FIPS_NAME')
        #rtVal.append('Year')
    elif category=='Climate and Economic Justice Screening Tool' :
        rtVal.append('DF_PFS')
        rtVal.append('AF_PFS')
        rtVal.append('HDF_PFS')
        rtVal.append('DSF_PFS')
        rtVal.append('EBF_PFS')
        rtVal.append('EALR_PFS')
        rtVal.append('EBLR_PFS')
        rtVal.append('EPLR_PFS')
        rtVal.append('HBF_PFS')
        rtVal.append('LLEF_PFS')
        rtVal.append('LIF_PFS')
        rtVal.append('LMI_PFS')
        rtVal.append('MHVF_PFS')
        rtVal.append('PM25F_PFS')
        rtVal.append('HSEF')
        rtVal.append('P100_PFS')
        rtVal.append('P200_PFS')
        rtVal.append('LPF_PFS')
        rtVal.append('NPL_PFS')
        rtVal.append('RMP_PFS')
        rtVal.append('TSDF_PFS')
        rtVal.append('TPF')
        rtVal.append('TF_PFS')
        rtVal.append('UF_PFS')
        rtVal.append('WF_PFS')
        rtVal.append('M_WTR')
        rtVal.append('M_WKFC')
        rtVal.append('M_CLT')
        rtVal.append('M_ENY')
        rtVal.append('M_TRN')
        rtVal.append('M_HSG')
        rtVal.append('M_PLN')
        rtVal.append('M_HLTH')
        rtVal.append('SM_C')
        rtVal.append('SM_PFS')
        rtVal.append('EPLRLI')
        rtVal.append('EALRLI')
        rtVal.append('EBLRLI')
        rtVal.append('PM25LI')
        rtVal.append('EBLI')
        rtVal.append('DPMLI')
        rtVal.append('TPLI')
        rtVal.append('LPMHVLI')
        rtVal.append('HBLI')
        rtVal.append('RMPLI')
        rtVal.append('SFLI')
        rtVal.append('HWLI')
        rtVal.append('WDLI')
        rtVal.append('DLI')
        rtVal.append('ALI')
        rtVal.append('HDLI')
        rtVal.append('LLELI')
        rtVal.append('LILHSE')
        rtVal.append('PLHSE')
        rtVal.append('LMILHSE')
        rtVal.append('ULHSE')
        rtVal.append('EPL_ET')
        rtVal.append('EAL_ET')
        rtVal.append('EBL_ET')
        rtVal.append('EB_ET')
        rtVal.append('PM25_ET')
        rtVal.append('DS_ET')
        rtVal.append('TP_ET')
        rtVal.append('LPP_ET')
        rtVal.append('HB_ET')
        rtVal.append('RMP_ET')
        rtVal.append('NPL_ET')
        rtVal.append('TSDF_ET')
        rtVal.append('WD_ET')
        rtVal.append('DB_ET')
        rtVal.append('A_ET')
        rtVal.append('HD_ET')
        rtVal.append('LLE_ET')
        rtVal.append('UN_ET')
        rtVal.append('LISO_ET')
        rtVal.append('POV_ET')
        rtVal.append('LMI_ET')
        rtVal.append('IA_LMI_ET')
        rtVal.append('IA_UN_ET')
        rtVal.append('IA_POV_ET')
        rtVal.append('TC')
        rtVal.append('CC')
        rtVal.append('IAULHSE')
        rtVal.append('IAPLHSE')
        rtVal.append('IALMILHSE')
        rtVal.append('IALMIL_87')
        rtVal.append('IAPLHS_88')
        rtVal.append('IAULHS_89')
        rtVal.append('LHE')
        rtVal.append('IALHE')
        rtVal.append('IAHSEF')
        rtVal.append('CA')
        rtVal.append('NCA')
        rtVal.append('CA_LT20')
        rtVal.append('M_CLT_EOMI')
        rtVal.append('M_ENY_EOMI')
        rtVal.append('M_TRN_EOMI')
        rtVal.append('M_HSG_EOMI')
        rtVal.append('M_PLN_EOMI')
        rtVal.append('M_WTR_EOMI')
        rtVal.append('M_HLTH_102')
        rtVal.append('M_WKFC_103')
        rtVal.append('FPL200S')
        rtVal.append('M_WKFC_105')
        rtVal.append('M_EBSI')
        rtVal.append('UI_EXP')
        rtVal.append('THRHLD')
    elif category=='Annual Climate' :
        rtVal.append('Annual_etr')
        rtVal.append('Annual_precipitation')
        rtVal.append('Annual_tempreture')
        rtVal.append('Aridity_index')
    elif category=='Cheat Grass' :
        rtVal.append('CheatGrass')
        rtVal.append('ExoticAnnualGrass')
        rtVal.append('Medusahead')
        rtVal.append('PoaSecunda')
    elif category=='Climate Normals' :
        rtVal.append('pr_Normal')
        rtVal.append('tmmn_Normal')
        rtVal.append('tmmx_Normal')
        rtVal.append('rmin_Normal')
        rtVal.append('rmax_Normal')
        rtVal.append('sph_Normal')
        rtVal.append('srad_Normal')
        rtVal.append('fm100_Normal')
        rtVal.append('fm1000_Normal')
        rtVal.append('bi_Normal')
        rtVal.append('vpd_Normal')
        rtVal.append('erc_Normal')
    elif category=='GRIDMET' :
        rtVal.append('pr')
        rtVal.append('tmmn')
        rtVal.append('tmmx')
        rtVal.append('rmin')
        rtVal.append('rmax')
        rtVal.append('sph')
        rtVal.append('vs')
        rtVal.append('th')
        rtVal.append('srad')
        rtVal.append('etr')
        rtVal.append('fm100')
        rtVal.append('fm1000')
        rtVal.append('bi')
        rtVal.append('vpd')
        rtVal.append('erc')
        rtVal.append('pr_5D_mean')
        rtVal.append('tmmn_5D_mean')
        rtVal.append('tmmx_5D_mean')
        rtVal.append('rmin_5D_mean')
        rtVal.append('rmax_5D_mean')
        rtVal.append('sph_5D_mean')
        rtVal.append('vs_5D_mean')
        rtVal.append('th_5D_mean')
        rtVal.append('srad_5D_mean')
        rtVal.append('etr_5D_mean')
        rtVal.append('fm100_5D_mean')
        rtVal.append('fm1000_5D_mean')
        rtVal.append('bi_5D_mean')
        rtVal.append('vpd_5D_mean')
        rtVal.append('erc_5D_mean')
        rtVal.append('pr_5D_min')
        rtVal.append('pr_5D_max')
        rtVal.append('tmmn_5D_max')
        rtVal.append('tmmx_5D_max')
        rtVal.append('rmin_5D_min')
        rtVal.append('rmax_5D_min')
        rtVal.append('sph_5D_min')
        rtVal.append('vs_5D_max')
        rtVal.append('th_5D_max')
        rtVal.append('srad_5D_max')
        rtVal.append('etr_5D_max')
        rtVal.append('fm100_5D_min')
        rtVal.append('fm1000_5D_min')
        rtVal.append('bi_5D_max')
        rtVal.append('vpd_5D_max')
        rtVal.append('erc_5D_max')
    elif category=='Climate Percentiles' :
        rtVal.append('tmmn_Percentile')
        rtVal.append('tmmx_Percentile')
        rtVal.append('sph_Percentile')
        rtVal.append('vs_Percentile')
        rtVal.append('fm100_Percentile')
        rtVal.append('bi_Percentile')
        rtVal.append('vpd_Percentile')
        rtVal.append('erc_Percentile')
    elif category=='Ecoregions' :
        rtVal.append('Ecoregion_US_L4CODE')
        rtVal.append('Ecoregion_US_L3CODE')
        rtVal.append('Ecoregion_NA_L3CODE')
        rtVal.append('Ecoregion_NA_L2CODE')
        rtVal.append('Ecoregion_NA_L1CODE')
    elif category=='Topography' :
        rtVal.append('Elevation')
        rtVal.append('Aspect')
        rtVal.append('Slope')
        rtVal.append('TPI')
        rtVal.append('TRI')
        rtVal.append('Elevation_1km')
        rtVal.append('Aspect_1km')
        rtVal.append('Slope_1km')
        rtVal.append('TPI_1km')
        rtVal.append('TRI_1km')
    elif category=='Vegetation' :
        rtVal.append('EVC')
        rtVal.append('EVC_1km')
        rtVal.append('EVH')
        rtVal.append('EVH_1km')
        rtVal.append('EVT')
        rtVal.append('EVT_1km')
    elif category=='Risk Management Assistance' :
        rtVal.append('Evacuation')
        rtVal.append('SDI')
    elif category=='Fire Regime Groups' :
        rtVal.append('FRG')
        rtVal.append('FRG_1km')
    elif category=='Fire Stations' :
        rtVal.append('No_FireStation_10km')
        rtVal.append('No_FireStation_50km')
        rtVal.append('No_FireStation_100km')
        rtVal.append('No_FireStation_200km')
    elif category=='Geographic Area Coordination Centers' :
        rtVal.append('GACCAbbrev')
        rtVal.append('GACC_PL')
        rtVal.append('GACC_New_fire')
        rtVal.append('GACC_New_LF')
        rtVal.append('GACC_Uncont_LF')
        rtVal.append('GACC_Type_1_IMTs')
        rtVal.append('GACC_Type_2_IMTs')
        rtVal.append('GACC_NIMO_Teams')
        rtVal.append('GACC_Area_Command_Teams')
        rtVal.append('GACC_Fire_Use_Teams')
    elif category=='Gap Analysis Project' :
        rtVal.append('Mang_Type')
        rtVal.append('Mang_Name')
        rtVal.append('Des_Tp')
        rtVal.append('GAP_Sts')
        rtVal.append('GAP_Prity')
    elif category=='Gross Domestic Product' :
        rtVal.append('GDP')
    elif category=='Global Human Modification' :
        rtVal.append('GHM')
    elif category=='MODIS NDVI' :
        rtVal.append('MOD_NDVI_12m')
        rtVal.append('MOD_EVI_12m')
    elif category=='NOAA NDVI' :
        rtVal.append('NDVI_min')
        rtVal.append('NDVI_max')
        rtVal.append('NDVI_mean')
        rtVal.append('NDVI1day')
    elif category=='National Land Cover Database' :
        rtVal.append('Land_Cover')
        rtVal.append('Land_Cover_1km')
    elif category=='National Preparedness Level' :
        rtVal.append('NPL')
    elif category=='Population' :
        rtVal.append('Population')
        rtVal.append('Popo_1km')
    elif category=='Pyrome' :
        rtVal.append('NAME')
    elif category=='Road' :
        rtVal.append('road_county_dis')
        rtVal.append('road_interstate_dis')
        rtVal.append('road_common_name_dis')
        rtVal.append('road_other_dis')
        rtVal.append('road_state_dis')
        rtVal.append('road_US_dis')
    elif category=='Social Vulnerability Index' :
        rtVal.append('RPL_THEMES')
        rtVal.append('RPL_THEME1')
        rtVal.append('EPL_POV')
        rtVal.append('EPL_UNEMP')
        rtVal.append('EPL_PCI')
        rtVal.append('EPL_NOHSDP')
        rtVal.append('RPL_THEME2')
        rtVal.append('EPL_AGE65')
        rtVal.append('EPL_AGE17')
        rtVal.append('EPL_DISABL')
        rtVal.append('EPL_SNGPNT')
        rtVal.append('RPL_THEME3')
        rtVal.append('EPL_MINRTY')
        rtVal.append('EPL_LIMENG')
        rtVal.append('RPL_THEME4')
        rtVal.append('EPL_MUNIT')
        rtVal.append('EPL_MOBILE')
        rtVal.append('EPL_CROWD')
        rtVal.append('EPL_NOVEH')
        rtVal.append('EPL_GROUPQ')
    elif category=='Rangeland Production Monitoring Service' :
        rtVal.append('rpms')
        rtVal.append('rpms_1km')
    elif category=='National Preperdness Level' :
        rtVal.append('NPL')
    return rtVal