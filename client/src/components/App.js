import React, { useEffect, useState } from "react";
import Login from "../pages/Login";

function App() {


  const [ attendee, setAttendee ] = useState(null)

  useEffect (() => {

    // need to check authorization
    fetch('/check_session')
      .then((r)=>{
        if (r.ok) {
          r.json()
          .then((attendee) => setAttendee(attendee))
        }
      }) 

  }, [])


  const handleLogout = () => {
    fetch('/logout', { method: 'DELETE'})
      .then((r) => {
        if (r.ok) {
          setAttendee(null)
        }
      })
  }


  if (!attendee) return <Login setAttendee={setAttendee}/>

  return (
  
    <div>
      <p>
        You are now logged in
      </p>
      <button onClick={handleLogout}> Logout </button>
    </div>
  );
}

export default App;
