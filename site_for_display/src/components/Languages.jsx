import React from 'react'
import styled from 'styled-components'
import flag_poland from '../assets/poland.png'
import flag_ukraine from '../assets/ukraine.png'
import flag_russia from '../assets/russia.png'
import {Link} from 'react-router-dom'

const Languages = () => {
  return (
    <section>
      <h2>Available languages</h2>
      <Flags>
        <Link to={'/Polish'}>
          <img src={flag_poland} alt="" />
        </Link>
        <Link to={'/Ukrainian'}>
          <img src={flag_ukraine} alt="" />
        </Link>
        <Link to={'/Russian'}>
          <img src={flag_russia} alt="" />
        </Link>
      </Flags>
    </section>
  )
}

const Flags = styled.div`
  display: flex;
  max-width: 80%;
  gap: 1rem;
  margin-left: auto;
  margin-right: auto;
  justify-content: center;

  img {
    margin: auto;
    display: block;
    border-radius: 0.5rem;
    width: 6rem;
    height: 4rem;
    object-fit: cover;
  }

`

export default Languages