import React from 'react'
import { SiMicrosoftexcel } from 'react-icons/si'
import styled from 'styled-components'
import Nav from '../components/Nav_RU.jsx'
import RU_Economy_ranking from '../assets/RU_economy_ranking.xlsx'
import RU_Economy_wd from '../assets/RU_economy_words_and_defs.xlsx'
import RU_Economy_log from '../assets/RU_economy_log.xlsx'
import RU_Politics_ranking from '../assets/RU_politics_ranking.xlsx'
import RU_Politics_wd from '../assets/RU_politics_words_and_defs.xlsx'
import RU_Politics_log from '../assets/RU_politics_log.xlsx'

function Russian() {
  return (
    <section>
      <h2>Russian</h2>
      <>
        <Nav/>
      </>
      <Body>
        <h3 id='economy'>I. Economy</h3>
        <h4>1. Information</h4>
        <Table>
          <tr>
            <th>Source</th>
            <td><a href="https://www.epravda.com.ua/rus/archives/">epravda.com.ua/rus/archives/</a></td>
          </tr>
          <tr>
            <th>Number of articles</th>
            <td>2301</td>
          </tr>
          <tr>
            <th>Number of words</th>
            <td>1060769</td>
          </tr>
          <tr>
            <th>Date published</th>
            <td>02/03/2022 - 01/05/2022</td>
          </tr>
          <tr>
            <th>Date retrieved</th>
            <td>01/05/2022</td>
          </tr>
        </Table>
        <h4>2. Resources</h4>
        <Table>
          <tr>
            <th>Most frequent words</th>
            <th>Words and definitions</th>
            <th>Source articles</th>
          </tr>
          <tr>
            <td><a href={RU_Economy_ranking} download='RU_economy_ranking.xlsx'><SiMicrosoftexcel/></a></td>
            <td><a href={RU_Economy_wd} download='RU_economy_words_and_defs.xlsx'><SiMicrosoftexcel/></a></td>
            <td><a href={RU_Economy_log} download='RU_economy_log.xlsx'><SiMicrosoftexcel/></a></td>
          </tr>
        </Table>
        <h3 id='politics'>II. Politics</h3>
        <h4>1. Information</h4>
        <Table>
          <tr>
            <th>Source</th>
            <td><a href="https://www.pravda.com.ua/rus/archives/">pravda.com.ua/rus/archives/</a></td>
          </tr>
          <tr>
            <th>Number of articles</th>
            <td>2434</td>
          </tr>
          <tr>
            <th>Number of words</th>
            <td>1019065</td>
          </tr>
          <tr>
            <th>Date published</th>
            <td>05/04/2022 - 30/04/2022</td>
          </tr>
          <tr>
            <th>Date retrieved</th>
            <td>30/04/2022</td>
          </tr>
        </Table>
        <h4>2. Resources</h4>
        <Table>
          <tr>
            <th>Most frequent words</th>
            <th>Words and definitions</th>
            <th>Source articles</th>
          </tr>
          <tr>
            <td><a href={RU_Politics_ranking} download='RU_Politics_ranking.xlsx'><SiMicrosoftexcel/></a></td>
            <td><a href={RU_Politics_wd} download='RU_Politics_words_and_defs.xlsx'><SiMicrosoftexcel/></a></td>
            <td><a href={RU_Politics_log} download='RU_Politics_log.xlsx'><SiMicrosoftexcel/></a></td>
          </tr>
        </Table>
      </Body>
    </section>
  )
}

export default Russian

const Body = styled.div`
  margin-left: auto;
  margin-right: auto;
  max-width: 80%;
  display: block;
  gap: 1rem;
  padding-bottom: 8rem;

  h3 {
    font-size: 1.5rem;
    padding: 1rem 0rem;
  }

  h4 { 
    padding-left: 1rem;
    padding-bottom: 0.5rem;
  }

  p {
    padding-bottom: 1.5rem;
  }
`

const Table = styled.table`
  width: 60%;
  min-width: 50%;
  margin-left: auto;
  margin-right: auto;
  text-align: center;
  padding: 2rem 0rem;

  th, td {
    border: 1px solid;
    border-color: var(--color-light);
    padding: 0.1rem 1rem;
  }

  th {
    background-color: var(--color-light);
    color: var(--color-bg);
  }

  td {
    background-color: transparent;
  }

  .empty {
    background-color: transparent;
    border: transparent;
  }

`