import React, { Component } from "react";
import RestaurantDataService from "../services/restaurant.service";
import { withRouter } from '../common/with-router';
import { Link } from "react-router-dom";


class Restaurant extends Component {
    constructor(props){
        super(props);

        this.state = {
            id: null,
            name: "",
            logo: "",
            dishes: []
        };
    }

    componentDidMount() {
        RestaurantDataService.get(this.props.router.params.id)
        .then(response => {
            this.setState({ 
                id: response.data.id,
                name: response.data.name, 
                logo: response.data.logo,
                dishes: response.data.dishes
            });
          })
          .catch(error => {
            console.log(error);
          });
    }
    render() {
        return (
          <div>
            <h1>Restaurant {this.state.name}</h1>
            <ul>
                <li><strong>Id:</strong> {this.state.id}</li>
                <li><strong>Name:</strong> {this.state.name}</li>
                <li><strong>Logo:</strong> {this.state.logo}</li>
            </ul>
            <h3>Dishes</h3>
            <table className="table">
                <thead>
                    <tr>
                        <th scope="col">Id</th>
                        <th scope="col">Name</th>
                        <th scope="col">Description</th>
                        <th scope="col">Price</th>
                    </tr>
                </thead>
                <tbody>
                    {
                        this.state.dishes.map((dish) => (
                            <tr key={dish.id}>
                                <td>{dish.id}</td>
                                <td>{dish.name}</td>
                                <td>{dish.description}</td>
                                <td>{dish.price}</td>
                                <td></td>
                            </tr>
                        ))
                    }
                </tbody>
            </table>
            <Link to={`/dish/add/${this.state.id}`} className="btn btn-warning">Add Dish</Link>
          </div>
        );
      }
}

export default withRouter(Restaurant);