import React from 'react'
import Home from './Home'
import Polish from './Polish'
import Ukrainian from './Ukrainian'
import Russian from './Russian'
import { Route, Routes } from 'react-router-dom'

const Pages = () => {
  return (
    <Routes>
        <Route path ='/' element={<Home/>}/>
        <Route path ='/Polish' element={<Polish/>}/>
        <Route path ='/Ukrainian' element={<Ukrainian/>}/>
        <Route path ='/Russian' element={<Russian/>}/>
    </Routes>
  )
}

export default Pages