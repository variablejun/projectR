
import React, { useEffect, useState } from 'react';
	import { makeStyles } from '@material-ui/core/styles';
	import Table from '@material-ui/core/Table';
	import TableBody from '@material-ui/core/TableBody';
	import TableCell from '@material-ui/core/TableCell';
	import TableContainer from '@material-ui/core/TableContainer';
	import TableHead from '@material-ui/core/TableHead';
	import TableRow from '@material-ui/core/TableRow';
	import Paper from '@material-ui/core/Paper';
	import Pagination from '@material-ui/lab/Pagination';
import {memberList} from 'api'

	const useStyles = makeStyles({
		table: {
		  minWidth: 650,
		},
		
	  });
	  const usePageStyles = makeStyles((theme) => ({
		  root: {
			'& > *': {
			  marginTop: theme.spacing(2),
			},
		  },
		}));
	  

	/*파이썬에서는 리스트로 던져주어야하는데 이미 컬럼이 정의되어있어(3차원) 한차원 낮은것으로 던져주어야한다 */
	
 const MemberList = () => {
	  const classes = useStyles();
	  const pageClasses = usePageStyles();
	  const [members, setMembers] = useState([]) // 상태 변환 파이썬에서 시리얼라이즈(직렬화)

	  useEffect(() => {
		memberList() // api index와 연결되어있는것
		.then(res => {
			
			setMembers(res.data)
		})
		.catch(err =>{
			console.log(err.data)
		})
	  }, [])
	   // 1번째 실행 유일하게 리턴보다 먼저실행, 특별한 이벤트 없이 실행
	  //2번째 실행
	  return (<>
		<TableContainer component={Paper}>
		  <Table className={classes.table} aria-label="simple table">
			<TableHead>
			  <TableRow> 
				<TableCell>회원 ID</TableCell>
				<TableCell align="right">비밀번호</TableCell>
				<TableCell align="right">회원 이름</TableCell>
				<TableCell align="right">이메일</TableCell>
			  </TableRow>
			</TableHead>
			<TableBody>
			  {
			  members.length != 0 // 3항연산 멤버스에 들어온값이 0이 아니라면
			  
			  ? members.map((member) => ( //참
			  <TableRow key={member.username}> 
			  <TableCell align="right">{member.username}</TableCell>
			  <TableCell component="th" scope="row">
			  {member.password}
			  </TableCell>
			  <TableCell align="right">{member.name}</TableCell>
			  <TableCell align="right">{member.email}</TableCell>

			  </TableRow>
			  ))
			  //거짓
			  :<TableRow> 
				<TableCell component="th" scope="row" colSpan="4">
					<h1>등록된 데이터가 없습니다.</h1>
				</TableCell>
			  
			  </TableRow>
			
			}
			  
			</TableBody>
		  </Table>
		</TableContainer>
		<div className={pageClasses.root}>
        <Pagination count={10} />
    </div>

		 </>
	  );
	 
}	
/* <TableCell component="th" scope="row">
					{row.name}
				  </TableCell>
				  <TableCell align="right">{row.calories}</TableCell>
				  <TableCell align="right">{row.fat}</TableCell>
				  <TableCell align="right">{row.carbs}</TableCell>
				  <TableCell align="right">{row.protein}</TableCell> */
export default MemberList