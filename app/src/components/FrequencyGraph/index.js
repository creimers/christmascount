import React from 'react'
import styled from 'styled-components'
import {LineChart, Line, XAxis, YAxis, Tooltip, Legend} from 'recharts';

const Container = styled.div`
  flex: ${props => props.show ? 1 : 0};
  transition: all 0.5s ease;
  overflow: hidden;
`

const HideRow = styled.div`
  display: flex;
  justify-content: flex-end;
  padding: 10px;
`

class FrequencyGraph extends React.Component {

  state = {
    timeSeries: []
  }
  
  fetchWordData = (word) => {
    const host = process.env.NODE_ENV === 'development' ? 'http://localhost:4000' : 'http://speechcount.superservice-international.com'

    fetch(`${host}/speeches/christmas-germany/${word}`)
      .then((response) => response.json())
      .then((json) => this.setState({timeSeries: json.series}))
  }

  componentWillReceiveProps(newProps) {
    if (newProps.selectedWord !== this.props.selectedWord) {
      this.fetchWordData(newProps.selectedWord)
    }
  }

  render() {
    return (
      <Container show={this.props.show}>
        <HideRow>
          <button onClick={this.props.onHide}>close</button>
        </HideRow>
        <h2>{this.props.selectedWord}</h2>
          <LineChart width={500} height={300} data={this.state.timeSeries}>
            <XAxis dataKey="year"/>
            <YAxis/>
            <Line type="monotone" dataKey="count" stroke="#8884d8" />
          </LineChart>
      </Container>
    )
  }
}

export default FrequencyGraph
