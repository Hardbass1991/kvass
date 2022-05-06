import React from 'react'
import styled from 'styled-components'

const Summary = () => {
  return (
    <section>
      <h2>Summary</h2>
      <Body>
        <p>So you might be wondering how I got those lists of words.</p>
        <p>The first step was scraping news websites for input text (details in every section)</p>
        <p>Then I analyzed the texts and found the number of occurrences for every word. To do this, I use the library Stanza in order to reduce every word to its basic form (lemmatization)</p>
        <p>After that I decided on a threshold of repetitions to retrieve only the most common words</p>
        <p>And well, along the process I also collected metadata also available on this website</p>
        <p>The actual code is in the Github link, in the footer.</p>
      </Body>
    </section>
  )
}

export default Summary

const Body = styled.div`
  margin: auto;
  width: 80%;
  text-align: justify;
  padding: 1rem;
`