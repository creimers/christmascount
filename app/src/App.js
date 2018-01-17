import React, { Component } from 'react';
import styled from 'styled-components'

import FrequencyGraph from './components/FrequencyGraph'
import FrequencyTable from './components/FrequencyTable'

const AppContainer = styled.div`
  height: 100vh;
  width: 100vw;
  overflow: hidden;
  display: flex;
  flex-direction: column;
`

class App extends Component {

  state = {
    showFrequencyGraph: false,
    selectedWord: 'menschen'
  }

  hideFrequencyGraph = () => {
    this.setState({showFrequencyGraph: false})
  }

  selectWord = (word) => {
    this.setState({selectedWord: word, showFrequencyGraph: true})
  }

  render() {
    return (
      <AppContainer>
        <FrequencyTable
          onSelect={this.selectWord}
          selectedWord={this.state.selectedWord}
        />
        <FrequencyGraph
          show={this.state.showFrequencyGraph}
          onHide={this.hideFrequencyGraph}
          selectedWord={this.state.selectedWord}
        />
      </AppContainer>
    );
  }
}

export default App;
