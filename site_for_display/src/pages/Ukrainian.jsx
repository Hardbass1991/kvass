import React from 'react'
import { SiMicrosoftexcel } from 'react-icons/si'
import styled from 'styled-components'
import Nav from '../components/Nav_UA.jsx'
import UA_Economy_ranking from '../assets/UA_economy_ranking.xlsx'
import UA_Economy_wd from '../assets/UA_economy_words_and_defs.xlsx'
import UA_Economy_log from '../assets/UA_economy_log.xlsx'
import UA_Politics_ranking from '../assets/UA_politics_ranking.xlsx'
import UA_Politics_wd from '../assets/UA_politics_words_and_defs.xlsx'
import UA_Politics_log from '../assets/UA_politics_log.xlsx'
import UA_History_ranking from '../assets/UA_history_ranking.xlsx'
import UA_History_wd from '../assets/UA_history_words_and_defs.xlsx'
import UA_History_log from '../assets/UA_history_log.xlsx'

function Ukrainian() {
  return (
    <section>
      <h2>Ukrainian</h2>
      <>
        <Nav/>
      </>
      <Body>
        <h3 id='economy'>I. Economy</h3>
        <h4>1. Information</h4>
        <Table>
          <tr>
            <th>Source</th>
            <td><a href="https://www.epravda.com.ua/archives/">epravda.com.ua/archives/</a></td>
          </tr>
          <tr>
            <th>Number of articles</th>
            <td>1938</td>
          </tr>
          <tr>
            <th>Number of words</th>
            <td>1072188</td>
          </tr>
          <tr>
            <th>Date published</th>
            <td>09/03/2022 - 01/05/2022</td>
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
            <td><a href={UA_Economy_ranking} download='UA_economy_ranking.xlsx'><SiMicrosoftexcel/></a></td>
            <td><a href={UA_Economy_wd} download='UA_economy_words_and_defs.xlsx'><SiMicrosoftexcel/></a></td>
            <td><a href={UA_Economy_log} download='UA_economy_log.xlsx'><SiMicrosoftexcel/></a></td>
          </tr>
        </Table>
        <h3 id='politics'>II. Politics</h3>
        <h4>1. Information</h4>
        <Table>
          <tr>
            <th>Source</th>
            <td><a href="https://www.pravda.com.ua/archives/">pravda.com.ua/archives/</a></td>
          </tr>
          <tr>
            <th>Number of articles</th>
            <td>1765</td>
          </tr>
          <tr>
            <th>Number of words</th>
            <td>1088346</td>
          </tr>
          <tr>
            <th>Date published</th>
            <td>14/04/2022 - 01/05/2022</td>
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
            <td><a href={UA_Politics_ranking} download='UA_Politics_ranking.xlsx'><SiMicrosoftexcel/></a></td>
            <td><a href={UA_Politics_wd} download='UA_Politics_words_and_defs.xlsx'><SiMicrosoftexcel/></a></td>
            <td><a href={UA_Politics_log} download='UA_Politics_log.xlsx'><SiMicrosoftexcel/></a></td>
          </tr>
        </Table>
        <h3 id='history'>III. History</h3>
        <h4>1. Information</h4>
        <Table>
          <tr>
            <th>Source</th>
            <td><a href="https://www.istpravda.com.ua/articles/">istpravda.com.ua/articles/</a></td>
          </tr>
          <tr>
            <th>Number of articles</th>
            <td>261</td>
          </tr>
          <tr>
            <th>Number of words</th>
            <td>1008726</td>
          </tr>
          <tr>
            <th>Date published</th>
            <td>14/01/2021 - 09/02/2022</td>
          </tr>
          <tr>
            <th>Date retrieved</th>
            <td>03/05/2022</td>
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
            <td><a href={UA_History_ranking} download='UA_history_ranking.xlsx'><SiMicrosoftexcel/></a></td>
            <td><a href={UA_History_wd} download='UA_history_words_and_defs.xlsx'><SiMicrosoftexcel/></a></td>
            <td><a href={UA_History_log} download='UA_history_log.xlsx'><SiMicrosoftexcel/></a></td>
          </tr>
        </Table>
      </Body>
    </section>
  )
}

export default Ukrainian

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