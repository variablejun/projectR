import React, {useEffect, useState} from 'react'
import axios from 'axios';
import { Button } from '@material-ui/core';

const Home = ({children}) => { 
    const [connection, setConnection] = useState(false)
    /*
    useEffect(()=>{
        
    },[])
    */
    /* 연결버튼 클릭..? */
    const handlecilck = e => {
        e.preventDefault()
        axios({
            method: "get",
            url: "http://127.0.0.1:8000/connection",
            responseType: "json"
        }).then(function (res) {
            setConnection(res.data.connection==='SUCCESS') /*데이터프레임이 넘어오는데 키가 커넥션, data가 data*/

        });
        
    }
    return (<>
    
    <table className="tab_lay">
        <tr><td><h1>홈</h1></td></tr>
        <tr><td><button color="primary" onClick ={handlecilck}>서버 연결 테스트</button></td></tr>
        <tr><td>{connection?
        "연결상태입니다." : "연결상태가아닙니다."}</td></tr>
        
    </table>
    {children}

</>)}


export default Home
