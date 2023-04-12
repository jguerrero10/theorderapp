import React, { Component } from "react";
import DishDataService from "../services/dish.service";
import { Link } from "react-router-dom";
import { withRouter } from '../common/with-router';

class AddDish extends Component {
    constructor(props) {
      super(props);
      this.onChangeName = this.onChangeName.bind(this);
      this.onChangeDescription = this.onChangeDescription.bind(this);
      this.onChangePrice = this.onChangePrice.bind(this);
      this.saveDish = this.saveDish.bind(this);
      this.newDish= this.newDish.bind(this);
  
      this.state = {
        id: null,
        name: "",
        description: "",
        price: null,
        restaurant_id: null,
        submitted: false
      };
    }
  
    onChangeName(e) {
      this.setState({
        name: e.target.value
      });
    }
  
    onChangeDescription(e) {
      this.setState({
        description: e.target.value
      });
    }

    onChangePrice(e) {
        this.setState({
            price: e.target.value
        });
      }
  
    saveDish() {
      var data = {
        name: this.state.name,
        description: this.state.description,
        restaurant_id: this.props.router.params.id,
        price: this.state.price
      };
  
      DishDataService.create(data)
        .then(response => {
          this.setState({
            id: response.data.id,
            name: response.data.name,
            description: response.data.logo,
            restaurant_id: response.data.restaurant_id,
            price: response.data.price,
            submitted: true
          });
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    }
  
    newDish() {
      this.setState({
        id: null,
        name: "",
        description: "",
        restaurant_id: null,
        price: null
      });
    }
  
    render() {
      return(
        <div className="submit-form">
        {this.state.submitted ? (
          <div>
            <h4>You submitted successfully!</h4>
            <Link to={`/restaurants/${this.state.restaurant_id}`} className="btn btn-warning">Ver</Link>
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
                name="name"
              />
            </div>

            <div className="form-group">
              <label htmlFor="logo">Description</label>
              <input
                type="text"
                className="form-control"
                id="description"
                required
                value={this.state.description}
                onChange={this.onChangeDescription}
                name="description"
              />
            </div>

            <div className="form-group">
              <label htmlFor="logo">Price</label>
              <input
                type="number"
                className="form-control"
                id="price"
                required
                value={this.state.price}
                onChange={this.onChangePrice}
                name="price"
              />
            </div>

            <button onClick={this.saveDish} className="btn btn-success mt-2">
              Submit
            </button>
          </div>
        )}
      </div>
      );
    }
  }

  export default withRouter(AddDish);