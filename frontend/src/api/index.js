import axios from "axios";

const SERVER = 'http://127.0.0.1:8000/'
const headers = {'Content-Type' : 'application/json'}
//각각의 DDLMRR에다 엑시오스를 잡아준다.
export const postDetail = body => axios.post(`${SERVER}api/post/detail`,{headers, body})
export const postDelete = body => axios.post(`${SERVER}api/post/delete`,{headers, body})
export const postList = body => axios.post(`${SERVER}api/post/list`,{headers, body})
export const postModify = body => axios.post(`${SERVER}api/post/modify`,{headers, body})
export const postRegister = body => axios.post(`${SERVER}api/post/register`,{headers, body})
export const postRetrieve = body => axios.post(`${SERVER}api/post/retrieve`,{headers, body})

export const itemDetail = body => axios.post(`${SERVER}item/detail`,{headers, body})
export const itemDelete = body => axios.post(`${SERVER}item/delete`,{headers, body})
export const itemList = body => axios.post(`${SERVER}item/list`,{headers, body})
export const itemModify = body => axios.post(`${SERVER}item/modify`,{headers, body})
export const itemRegister = body => axios.post(`${SERVER}item/register`,{headers, body})
export const itemRetrieve = body => axios.post(`${SERVER}item/retrieve`,{headers, body})

export const memberDetail = id => axios.get(`${SERVER}api/member/detail/${id}`)
export const memberDelete = id => axios.delete(`${SERVER}api/member/delete/${id}`)
export const memberList = () => axios.get(`${SERVER}adm/member/list`) // return이 있는 함수 이다. 값을 받아 멤버리스트에 넣어주고 그걸 ml에 부려준다 함수이름은 곧 함수의 리턴값을 나타낸다. 
// LIst는 값을 바로 받아와얗 하기때문에 비워놓는다. 전선처럼 항상 연결되어있지만 이벤트를 작동시키지 않으면 작동하지 않음(이벤트 드리븐) -> 비동기식
//  -> url로 연결되어있다.
export const memberModify = body => axios.put(`${SERVER}api/member/modify`,{headers, body})
export const memberRegister = body => axios.post(`${SERVER}api/member/register`,{headers, body})
export const memberRetrieve = body => axios.get(`${SERVER}adm/member/retrieve`,{headers, body})
export const memberLogin = body => axios.post(`${SERVER}api/member/login`,{headers, body}) // 값을 보내가도 하고 받기도 한다 서로 함수로써 연결되어있다. 함수