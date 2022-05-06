import React from 'react'
import styled from 'styled-components'
import country_balls from '../assets/country_balls.png'
import {BsTwitter} from 'react-icons/bs'
import {BsGithub} from 'react-icons/bs'
import {BsYoutube} from 'react-icons/bs'

const Footer = () => {
  return (
    <section>
        <Tm>HardBass1991&trade;. All rights reserved.</Tm>
        <Pic>
            <a href="https://twitter.com/realDonaldTrump"><BsTwitter/></a>
            <a href="https://github.com/Hardbass1991/kvass"><BsGithub/></a>
            <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"><BsYoutube/></a>
        </Pic>
    </section>
  )
}


const Pic = styled.div`
    margin-left: auto;
    margin-right: auto;
    border-radius: 2rem;
    max-width: 30%;
    overflow: hidden;
    gap: 1rem;
    display: flex;
    justify-content: center;
    padding-bottom: 10rem;
`
const Tm = styled.div`
    text-align: center;
    padding-bottom: 1rem;
`
export default Footer