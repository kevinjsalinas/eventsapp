import React from 'react'

function SignupForm() {
  return (


    <div>
        <form>
            <label>email</label>
            <input 
                type="email"
                id= "email"
            >
            </input>
            <label>password</label>
            <input 
                type="password"
                id = "password"
            >
            </input>
            <button>Sign Up</button>
        </form>
    </div>
  )
}

export default SignupForm
