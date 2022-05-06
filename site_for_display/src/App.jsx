import React from 'react'
import styled from 'styled-components'
import Header from './components/Header'
import Pages from './pages/Pages'
import Footer from './components/Footer'
import { BrowserRouter } from 'react-router-dom';


const App = () => {
    return (
        <BrowserRouter>
            <Header/>
            <Pages/>
            <Footer/>
        </BrowserRouter>
    );
}

export default App