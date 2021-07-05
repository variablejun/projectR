import React,{useState} from 'react'
//import './Signup.css'
import { memberRegister, memberLogin} from 'api'
import { Button } from '@material-ui/core';
import{ useHistory} from 'react-router'

const MemberRegister = () => {
  const history = useHistory()

  const [memberInfo, setMemberinfo] = useState({
    username: '',
    password: '',
    name: '',
    email:'',


  })
  const {username, password, name, email} = 'userInfo' /*구조분해할당*/ 

  const handleChange = e =>{
    const {name, value} = e.target
    setMemberinfo({ 
      ...memberInfo,// 입력한 값을지우지말고 계속 저장해서 가져가라
      [name]: value
    })
  } 

  const handleSubmit = e =>{ //  submit 한개의 데이터를 전송할때
    e.preventDefault()
    let handleErrors = response =>{
      if(!response.ok){
        throw Error(response.statusText)
      }
      return response;
    }
    alert(`전송 클릭: ${JSON.stringify({...memberInfo})}`)
    memberRegister({...memberInfo})
    .then(res => {
      alert(`회원가입 완료 : ${res.data.result}`)

    }) //성공
    .catch(err =>{
      alert(`회원가입 실패 : ${err}`)
    }) //실패
    
    const loginRequest = {...memberInfo}
    memberLogin(loginRequest) // Promise 코딩패턴
    .then()
    .catch()
  } 

  const handleClick = e =>{ // click 여러개 데이터를 결합하여 전송할때
    e.preventDefault()
    alert('취소 클릭')
  }

    return (<>
    <div className = "Signup">
    <form onSubmit={handleSubmit} method = "post" style={{border:"1px solid #ccc"}}>
    <div className="container">
    <h1>Sign Up</h1>
    <p>Please fill in this form to create an account.</p>
    <hr/>

    <label for="username"><b>User ID</b></label>
    <input type="text" placeholder="Enter ID" onChange={handleChange} name="username" value = {username}/>

    <label for="password"><b>Password</b></label>
    <input type="password" placeholder="Enter Password" onChange={handleChange} name="password" value = {password}/>

    <label for="name"><b>Name</b></label>
    <input type="text" placeholder="Enter Your Name" onChange={handleChange} name="name" value = {name}/>
    
    <label for="email"><b>Email</b></label>
    <input type="text" placeholder="Enter Email" onChange={handleChange} name="email" value = {email}/>

    <p>By creating an account you agree to our <a href="#" style={{color:"dodgerblue"}}>Terms & Privacy</a>.</p>

    <div class="clearfix">
      <button type="button" className="canclebtn" onClick={handleClick}>Cancel</button>
      <button type="submit" className="signupbtn" >Sign Up</button>
      
    </div>
  </div>

</form>
</div>
</>)
}

export default MemberRegister