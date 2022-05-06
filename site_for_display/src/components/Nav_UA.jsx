import React from 'react'
import {AiOutlineHome} from 'react-icons/ai'
import {useState} from 'react'
import styled from 'styled-components'

const Nav = () => {
  const [activeNav, setActiveNav] = useState('#')
  return (
    <Wrapper>
      <a href="#" onClick={() => setActiveNav('#')} className={activeNav === '#' ? 'active' : ''}><AiOutlineHome/></a>
      <a href="#economy" onClick={() => setActiveNav('#economy')} className={activeNav === '#economy' ? 'active' : ''}>Economy</a>
      <a href="#politics" onClick={() => setActiveNav('#politics')} className={activeNav === '#politics' ? 'active' : ''}>Politics</a>
      <a href="#history" onClick={() => setActiveNav('#history')} className={activeNav === '#history' ? 'active' : ''}>History</a>
    </Wrapper>
  )
}

export default Nav

const Wrapper = styled.nav`
  height: auto;
  width: max-content;
  padding: 0.7rem 1.7rem;
  position: fixed;
  left: 50%;
  transform: translateX(-50%);

  display: flex;
  gap: 0.8rem;
  border-radius: 1rem;
  background: rgba(0, 0, 0, 0.3);
  backdrop-filter: blur(15px);

  a {
  background: transparent;
  padding: 0.9rem;
  border-radius: 1rem;
  display: flex;
  color: var(--color-light);
  font-size: 1.1rem;
  }

  a:hover {
    background: rgba(0, 0, 0, 0.3);
  }

  a.active {
    background: var(--color-primary);
    color: var(--color-bg);
}

`