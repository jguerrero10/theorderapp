import React, { Component } from "react";
import RestaurantDataService from "../services/restaurant.service";
import { Link } from "react-router-dom";

export default class AddRestaurant extends Component {
    constructor(props) {
      super(props);
      this.onChangeName = this.onChangeName.bind(this);
      this.onChangeLogo = this.onChangeLogo.bind(this);
      this.saveRestaurant = this.saveRestaurant.bind(this);
      this.newRestaurant= this.newRestaurant.bind(this);
  
      this.state = {
        id: null,
        name: "",
        logo: "",
        submitted: false
      };
    }
  
    onChangeName(e) {
      this.setState({
        name: e.target.value
      });
    }
  
    onChangeLogo(e) {
      this.setState({
        logo: e.target.value
      });
    }
  
    saveRestaurant() {
      console.log(this.state.name);
      console.log(this.state.logo);
      var data = {
        name: this.state.name,
        logo: this.state.logo
      };
  
      RestaurantDataService.create(data)
        .then(response => {
          this.setState({
            id: response.data.id,
            name: response.data.name,
            logo: response.data.logo,

            submitted: true
          });
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    }
  
    newRestaurant() {
      this.setState({
        id: null,
        name: "",
        logo: ""
      });
    }
  
    render() {
      return(
        <div className="submit-form">
        {this.state.submitted ? (
          <div>
            <h4>You submitted successfully!</h4>
            <Link to={"/restaurants/"} className="btn btn-primary">View Restaurant</Link>
          </div>
        ) : (
          <div>
            <div className="form-group">
              <label htmlFor="name">Name</label>
              <input
                type="text"
                className="form-control"
                id="name"
                required
                value={this.state.name}
                onChange={this.onChangeName}
                name="name"ddDish 
              />
            </div>

            <div className="form-group">
              <label htmlFor="logo">Logo</label>
              <input
                type="text"
                className="form-control"
                id="logo"
                required
                value={this.state.logo}
                onChange={this.onChangeLogo}
                name="logo"
              />
            </div>

            <button onClick={this.saveRestaurant} className="btn btn-success mt-2">
              Submit
            </button>
          </div>
        )}
      </div>
      );
    }
  }