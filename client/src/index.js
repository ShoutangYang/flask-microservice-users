import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import './index.css';
// import App from './App';
import axios from 'axios';
import * as serviceWorker from './serviceWorker';
import UserList from './components/UserList';

const URL = 'http://127.0.0.1:5001';

class App extends Component {
	constructor() {
		super();
		this.state = {
			users: []
		};
	}
	componentDidMount() {
		this.getUsers();
	}
	getUsers() {
		axios
			.get('http://0.0.0.0:5001/users')
			.then((res) => {
				this.setState({
					users: res.data.data.users
				});
				console.log(res.data.data.users);
			})
			.catch((err) => {
				console.log(err);
			});
	}
	render() {
		return (
			<div className="container">
				<div className="row">
					<div className="col-md-4">
						<br />
						<h1> All Users</h1>
						<hr />
						<br />
						<UserList users={this.state.users} />
					</div>
				</div>
			</div>
		);
	}
}
ReactDOM.render(<App />, document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: http://bit.ly/CRA-PWA
serviceWorker.unregister();
