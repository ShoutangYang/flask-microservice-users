import React from 'react'
import { shallow } from 'enzyme'
import UserList from './UserList'


const users = [
    {
        'active':true,
        'email':'to_tsy@163.com',
        'id':1,
        'username':'to_tsy'
    },
    {
        'active':true,
        'email':'to_yst@163.com',
        'id':2,
        'username':'to_yst'
    }
]

test('Userlist renders property',()=>{
    const wrapper = shallow(<UserList users={users}/>);
    const element = wrapper.find('h4');
    expect(element.length).toBe(2);
    expect(element.get(0).props.className).toBe('well');
    expect(element.get(0).props.children).toBe('to_tsy');
} )