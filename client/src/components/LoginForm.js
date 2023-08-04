import React, { useState } from 'react'


function LoginForm ( {setAttendee} ) {

    const [ email, setEmail ] = useState("")
    const [ password, setPassword ] = useState("")

    //handleSubmitLogin
    const handleSubmit = (e) => {

        e.preventDefault()

        fetch('/login', {
            method: 'POST',
            headers: {
            'Content-Type': 'application/json',
            },
            body: JSON.stringify({ email, password }),
        })
            .then((r) => {
                if (r.ok) {
                    r.json().then((attendee) => setAttendee(attendee))
                }
            })
        
    }

  return (
    <div>
        <form onSubmit={handleSubmit}>
            <label>email</label>
            <input 
                type="email"
                id= "email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
            >
            </input>
            <label>password</label>
            <input 
                type="password"
                id = "password"
                value = {password}
                onChange={(e) => setPassword(e.target.value)}
            >
            </input>
            <button>login</button>
        </form>
    </div>
  )
}

export default LoginForm





