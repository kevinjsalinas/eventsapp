import React, { useEffect, useState } from "react";
import LoginForm from "./LoginForm";

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


  if (!attendee) return <LoginForm setAttendee={setAttendee}/>

  return (
  
    <div>
      You are now logged in
    </div>
  );
}

export default App;
