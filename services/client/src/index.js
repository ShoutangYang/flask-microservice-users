import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import './index.css';
// import App from './App';
import axios from 'axios';
import * as serviceWorker from './serviceWorker';
import UserList from './components/UserList';
import AddUser from './components/AddUser';

const URL = 'http://127.0.0.1:5001';

class App extends Component {
	constructor() {
		super();
		this.state = {
			users: [],
			username: 'test_01',
			email: ''
		};
		this.addUser = this.addUser.bind(this);
		this.handleChange = this.handleChange.bind(this);
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

	addUser(event) {
		event.preventDefault();
		console.log(' check');
		console.log(this.state);
		const data = {
			username: this.state.username,
			email: this.state.email
		};
		axios
			.post('http://0.0.0.0:5001/users', data)
			.then((res) => {
				console.log(res);
				this.getUsers();
				this.setState({username:'',email:''})
				
			})
			.catch((err) => {
				console.log(err);
			});
	}

	handleChange(event) {
		const obj = {};
		obj[event.target.name] = event.target.value;
		this.setState(obj);
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
						<AddUser
							addUser={this.addUser}
							email={this.state.email}
							username={this.state.username}
							handleChange={this.handleChange}
						/>
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
