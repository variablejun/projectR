import React, { useState } from 'react'
//import './Login.css'
import { Button } from '@material-ui/core'
import {memberLogin}from 'api'
const MemberLogin = () => {
  const [login, setLogin] = useState({
    username :'',
    password : '',

})
  
  const {username, password} = login

  const handleClick = e => {
    e.preventDefault()
  }
  const handleSubmit = e => {
    e.preventDefault()
    let handleErrors = response =>{
      if(!response.ok){
        throw Error(response.statusText)
      }
      return response;
    }
    
    const {name, value} = e.target
    setLogin({
        ...login,
        [name] : value
    })
    alert(`전송 클릭: ${JSON.stringify({...login})}`)
    memberLogin({...login})
    .then(res => {
      alert(`작성 완료: ${res.data.result}`)

    }) //성공
    .catch(err =>{
      alert(`작성 실패 : ${err}`)
    }) //실패
  }
  const handleChange = e => {
    e.preventDefault()
}

return (<>
    <h2>Login Form</h2>
<div className="Login">
<form onSubmit = {handleSubmit} action="/action_page.php" method="get">
  
    <label for="username"><b>Username</b></label>
    <input type="text" placeholder="Enter Username" onChange={handleChange} name="username" value = {username} />

    <label for="password"><b>Password</b></label>
    <input type="text" placeholder="Enter Password" onChange={handleChange} name="password" value = {password} />
     
  
    <button type="submit" className="signupbtn">Login</button>
    <button type="button" className="cancelbtn" onClick={handleClick}>Cancel</button>
    
  
</form>
</div>
  </>)
}

export default MemberLogin