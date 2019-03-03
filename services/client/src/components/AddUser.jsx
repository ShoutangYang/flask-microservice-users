import React from 'react';

const AddUser = (props) => {
	return (
		<form onSubmit={(event)=> props.addUser(event)} className="form-group">
			<div>
				<input
					type="text"
					name="username"
					className="form-control input-lg"
					placeholder="Enter a username"
					required
					value={props.username}
					onChange = {props.handleChange}
				/>
			</div>
			<div className="form-group">
				<input
					type="text"
					name="email"
					className="form-control input-lg"
					type="email"
					placeholder="Enter an email address"
					required
					value={props.email}
					onChange = {props.handleChange}
				/>

				<input type="submit" className="btn btn-primary btn-lg btn-block" value="Submit" />
			</div>
		</form>
	);
};
export default AddUser;
