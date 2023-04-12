import React, {Component} from "react";
import { Routes, Route, Link } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";
import "./App.css";

import AddRestaurant from "./components/add-restaurant.component";
import RestaurantList  from "./components/list-restaurant.component"
import Restaurant from "./components/get-restaurant.component";
import AddDish from "./components/add-dish.component";

class App extends Component {
	render(){
		return(
			<div>
				<nav className="navbar navbar-expand navbar-dark bg-dark">
					<Link to={"/"} className="navbar-brand">
						The Order App
					</Link>
					<div className="navbar-nav mr-auto">
						
					</div>
				</nav>

				<div className="container mt-3">
					<Routes>
						<Route path="/" />
						<Route path="/restaurants"  element={< RestaurantList  />} />
						<Route path="/restaurants/add"  element={<AddRestaurant />}/>
						<Route path="/restaurants/:id" element={< Restaurant />} />
						<Route path="/dish/add/:id" element={< AddDish/>}/>
					</Routes>
				</div>
			</div>
    	);
 	}
}

export default App;
