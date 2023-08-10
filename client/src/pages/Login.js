import React, { useState } from 'react'
import LoginForm from '../components/LoginForm'
import SignupForm from '../components/SignupForm'


function Login( { onLogin }) {

    const [showLogin, setShowLogin] = useState(true)


  return (
    <div>

        { showLogin ? (
            <>
                <LoginForm onLogin={onLogin}  />
                <p>don't have an account?</p>
                <button onClick={() => setShowLogin(false)}>Sign Up</button>
            
            </>
        ): (
            <>

                <SignupForm/>
                <p>already have an account?</p>
                <button onClick={() => setShowLogin(true)}>Login</button>
            
            </>
            
        )}
      
    </div>
  )
}

export default Login
