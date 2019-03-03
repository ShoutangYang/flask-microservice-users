import React, { Component } from 'react';

const UserList = (props) => {
	return (
		<div>
			{props.users.map((users) => {
				return (
					<h4 key={users.id} className="well">
						{users.username}
					</h4>
				);
			})}
		</div>
	);
};

export default UserList;
