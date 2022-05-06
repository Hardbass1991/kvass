import React from 'react'
import styled from 'styled-components'
import {Link} from 'react-router-dom'

const Header = () => {
  return (
    <section>
        <div>
            <Title>
                <Link to='/'>
                    <h1>Undeclinator-Accumulator of Slavic words</h1>
                </Link>
            </Title>
            
            <Paraf>
                Hello, fellow language learner! This website aims to provide a useful tool for quicker adquisition of vocabulary.
            </Paraf>
            <Paraf>
                So far, there are three languages available and several sections per language. 
            </Paraf>
            <Paraf>
                Every section of a language provides the most common words for that language and subject. 
            </Paraf>
        </div>
    </section>
  )
}

export default Header

const Title = styled.div`
    text-align: center;
    padding: 2rem
`

const Paraf = styled.p`
    text-align: center;
    padding: 0 1rem;
`


