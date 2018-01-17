import React from 'react'
import styled from 'styled-components'


const Container = styled.div`
  flex: 1;
  background: lightgrey;
  overflow-y: scroll;
`

const Tr = styled.tr`
  cursor: pointer;
`

class FrequencyTable extends React.Component {

  state = {frequencies: []}
  
  componentDidMount() {
    const host = process.env.NODE_ENV === 'development' ? 'http://localhost:4000' : 'http://speechcount.superservice-international.com'

    fetch(`${host}/speeches/christmas-germany`)
      .then((response) => response.json())
      .then((json) => this.setState({frequencies: json.data}))
  }

  renderTable = () => {
    return (
      <table>
        <thead>
          <tr>
            <th>word</th>
            <th>frequency</th>
          </tr>
        </thead>
        <tbody>
          {this.state.frequencies.map((f, index) => {
            return (
              <Tr key={index} onClick={() => this.props.onSelect(f[1])}>
                <td>{f[1]}</td>
                <td>{f[0]}</td>
              </Tr>
            )
          })}
        </tbody>
      </table>
    )
  }

  render() {
    return (
      <Container>
        {this.renderTable()}
      </Container>
    )
  }
}

export default FrequencyTable
