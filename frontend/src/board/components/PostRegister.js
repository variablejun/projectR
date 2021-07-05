import React,{useState} from 'react'
// import './Postwrite.css'
import { postRegister,memberLogin } from 'api'
import { Button } from '@material-ui/core';
import{ useHistory} from 'react-router'
import { Tune } from '@material-ui/icons';

const Postwrite = () => {
  const history = useHistory()

  const [userInfo, setuserinfo] = useState({
  title: '',
  content: '',
	create_at: new Date(),
	update_at: new Date(),

  })
  const {title, content} = 'userInfo' /*구조분해할당*/ 

  const handleChange = e =>{
    const {name, value} = e.target
    setuserinfo({ 
      ...userInfo,// 입력한 값을지우지말고 계속 저장해서 가져가라
      [name]: value // 추가되는 키와 벨류는 계속 추가해줘라
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
    alert(`전송 클릭: ${JSON.stringify({...userInfo})}`)
    postRegister({...userInfo})
    .then(res => {
      alert(`작성 완료: ${res.data.result}`)

    }) //성공
    .catch(err =>{
      alert(`작성 실패 : ${err}`)
    }) //실패
    
    const loginRequest = {...userInfo}
    memberLogin(loginRequest) // Promise 코딩패턴
    .then()
    .catch()
  } 

  const handleClick = e =>{ // click 여러개 데이터를 결합하여 전송할때
    e.preventDefault() // 순수 js(바닐라스크립트) 작동을 막는다.
    alert('취소 클릭')
  }

    return (<>
    <div className = "postwrite">
    <form onSubmit={handleSubmit} method = "post" style={{border:"1px solid #ccc"}}>
    <div className="container">
    <h1>게시글 쓰기</h1>
    <p>Please fill in this form to create an account.</p>
    <hr/>

    <label for="title"><b>Title</b></label>
    <input type="text" placeholder="Enter Title" onChange={handleChange} name="title" value = {title}/>

    <label for="content"><b>Content</b></label>
    <input type="text" placeholder="Enter Content" onChange={handleChange} name="content" value = {content}/>

    <div class="clearfix">
      <button type="button" className="canclebtn" onClick={handleClick}>Cancel</button>
      <button type="submit" className="signupbtn" >Sign Up</button>
      
    </div>
  </div>
</form>
</div>
</>)
}

export default Postwrite