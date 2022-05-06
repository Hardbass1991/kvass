import React from 'react'
import styled from 'styled-components'
import { Link } from 'react-router-dom'
import { BsCheckLg } from 'react-icons/bs'

const Map = () => {
  return (
    <section>
      <h2>Map</h2>
      <Table>
        <tr>
          <th class='empty'></th>
          <th>Polish</th>
          <th>Ukrainian</th>
          <th>Russian</th>
        </tr>
        <tr>
          <th>Economy</th>
          <td><Link to={"/Polish#economy"}><BsCheckLg/></Link></td>
          <td><Link to={"/Ukrainian#economy"}><BsCheckLg/></Link></td>
          <td><Link to={"/Russian#economy"}><BsCheckLg/></Link></td>
        </tr>
        <tr>
          <th>Politics</th>
          <td><Link to={"/Polish#politics"}><BsCheckLg/></Link></td>
          <td><Link to={"/Ukrainian#politics"}><BsCheckLg/></Link></td>
          <td><Link to={"/Russian#politics"}><BsCheckLg/></Link></td>
        </tr>
        <tr>
          <th>History</th>
          <td></td>
          <td><Link to={"/Ukrainian#history"}><BsCheckLg/></Link></td>
          <td></td>
        </tr>
        <tr>
          <th>Culture</th>
          <td><Link to={"/Polish#culture"}><BsCheckLg/></Link></td>
          <td></td>
          <td></td>
        </tr>
        <tr>
          <th>World</th>
          <td><Link to={"/Polish#world"}><BsCheckLg/></Link></td>
          <td></td>
          <td></td>
        </tr>
      </Table>
    </section>
    
  )
}

const Table = styled.table`
  min-width: 50%;
  margin-left: auto;
  margin-right: auto;
  text-align: center;

  th, td {
    border: 1px solid;
    border-color: var(--color-light);
    padding: 0.1rem 1rem;
  }

  th {
    background-color: var(--color-bg);
  }

  td {
    background-color: var(--color-light);
    color: var(--color-bg);

    a {
    color: var(--color-bg);
    transition: var(--transition);
  }
    
    a:hover {
      color: var(--color-white);
    }
  }

  .empty {
    background-color: transparent;
    border: transparent;
  }



`

export default Map

