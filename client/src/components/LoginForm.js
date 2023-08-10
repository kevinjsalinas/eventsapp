import React, { useState } from 'react'


function LoginForm ( {onLogin} ) {

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
            body: JSON.stringify({email, password }),
        }).then((r) => {
                if (r.ok) {
                    r.json().then((attendee) => onLogin(attendee))
                } else {
                    alert('must enter a valid email and password')
                }
            })
        
    }

  return (
        <form onSubmit={handleSubmit}>
            <label>email</label>
            <input 
                type="email"
                id= "email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
            />
            <label>password</label>
            <input 
                type="password"
                id = "password"
                value = {password}
                onChange={(e) => setPassword(e.target.value)}
            />
            <button type='submit'>Login</button>
        </form>
  )
}

export default LoginForm





