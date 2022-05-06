import React from 'react'
import { SiMicrosoftexcel } from 'react-icons/si'
import styled from 'styled-components'
import Nav from '../components/Nav_PL.jsx'
import PL_Economy_ranking from '../assets/PL_economy_ranking.xlsx'
import PL_Economy_wd from '../assets/PL_economy_words_and_defs.xlsx'
import PL_Economy_log from '../assets/PL_economy_log.xlsx'
import PL_Country_ranking from '../assets/PL_country_ranking.xlsx'
import PL_Country_wd from '../assets/PL_country_words_and_defs.xlsx'
import PL_Country_log from '../assets/PL_country_log.xlsx'
import PL_World_ranking from '../assets/PL_world_ranking.xlsx'
import PL_World_wd from '../assets/PL_world_words_and_defs.xlsx'
import PL_World_log from '../assets/PL_world_log.xlsx'
import PL_Culture_ranking from '../assets/PL_culture_ranking.xlsx'
import PL_Culture_wd from '../assets/PL_culture_words_and_defs.xlsx'
import PL_Culture_log from '../assets/PL_culture_log.xlsx'


function Polish() {
  return (
    <section>
      <h2>Polish</h2>
      <>
        <Nav/>
      </>
      <Body>
        <h3 id='economy'>I. Economy</h3>
        <h4>1. Information</h4>
        <Table>
          <tr>
            <th>Source</th>
            <td><a href="https://krytykapolityczna.pl/gospodarka/">krytykapolityczna.pl/gospodarka/</a></td>
          </tr>
          <tr>
            <th>Number of articles</th>
            <td>719</td>
          </tr>
          <tr>
            <th>Number of words</th>
            <td>1051679</td>
          </tr>
          <tr>
            <th>Date published</th>
            <td>05/04/2012 - 19/04/2022</td>
          </tr>
          <tr>
            <th>Date retrieved</th>
            <td>28/04/2022</td>
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
            <td><a href={PL_Economy_ranking} download='PL_economy_ranking.xlsx'><SiMicrosoftexcel/></a></td>
            <td><a href={PL_Economy_wd} download='PL_economy_words_and_defs.xlsx'><SiMicrosoftexcel/></a></td>
            <td><a href={PL_Economy_log} download='PL_economy_log.xlsx'><SiMicrosoftexcel/></a></td>
          </tr>
        </Table>
        <h3 id='politics'>II. Politics</h3>
        <h4>1. Information</h4>
        <Table>
          <tr>
            <th>Source</th>
            <td><a href="https://krytykapolityczna.pl/kraj/">krytykapolityczna.pl/kraj/</a></td>
          </tr>
          <tr>
            <th>Number of articles</th>
            <td>839</td>
          </tr>
          <tr>
            <th>Number of words</th>
            <td>1070304</td>
          </tr>
          <tr>
            <th>Date published</th>
            <td>27/11/2020 - 29/04/2022</td>
          </tr>
          <tr>
            <th>Date retrieved</th>
            <td>02/05/2022</td>
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
            <td><a href={PL_Country_ranking} download='PL_country_ranking.xlsx'><SiMicrosoftexcel/></a></td>
            <td><a href={PL_Country_wd} download='PL_country_words_and_defs.xlsx'><SiMicrosoftexcel/></a></td>
            <td><a href={PL_Country_log} download='PL_country_log.xlsx'><SiMicrosoftexcel/></a></td>
          </tr>
        </Table>
        <h3 id='world'>III. World</h3>
        <h4>1. Information</h4>
        <Table>
          <tr>
            <th>Source</th>
            <td><a href="https://krytykapolityczna.pl/swiat/">krytykapolityczna.pl/swiat/</a></td>
          </tr>
          <tr>
            <th>Number of articles</th>
            <td>960</td>
          </tr>
          <tr>
            <th>Number of words</th>
            <td>1090839</td>
          </tr>
          <tr>
            <th>Date published</th>
            <td>09/07/2020 - 29/04/2022</td>
          </tr>
          <tr>
            <th>Date retrieved</th>
            <td>02/05/2022</td>
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
            <td><a href={PL_World_ranking} download='PL_world_ranking.xlsx'><SiMicrosoftexcel/></a></td>
            <td><a href={PL_World_wd} download='PL_world_words_and_defs.xlsx'><SiMicrosoftexcel/></a></td>
            <td><a href={PL_World_log} download='PL_world_log.xlsx'><SiMicrosoftexcel/></a></td>
          </tr>
        </Table>
        <h3 id='culture'>IV. Culture</h3>
        <h4>1. Information</h4>
        <Table>
          <tr>
            <th>Source</th>
            <td><a href="https://krytykapolityczna.pl/kultura/">krytykapolityczna.pl/kultura/</a></td>
          </tr>
          <tr>
            <th>Number of articles</th>
            <td>718</td>
          </tr>
          <tr>
            <th>Number of words</th>
            <td>1044077</td>
          </tr>
          <tr>
            <th>Date published</th>
            <td>09/01/2020 - 23/04/2022</td>
          </tr>
          <tr>
            <th>Date retrieved</th>
            <td>02/05/2022</td>
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
            <td><a href={PL_Culture_ranking} download='PL_culture_ranking.xlsx'><SiMicrosoftexcel/></a></td>
            <td><a href={PL_Culture_wd} download='PL_culture_words_and_defs.xlsx'><SiMicrosoftexcel/></a></td>
            <td><a href={PL_Culture_log} download='PL_culture_log.xlsx'><SiMicrosoftexcel/></a></td>
          </tr>
        </Table>
      </Body>
    </section>
  )
}

export default Polish

const Body = styled.div`
  margin-left: auto;
  margin-right: auto;
  max-width: 80%;
  display: block;
  gap: 1rem;
  padding-bottom: 1rem;

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