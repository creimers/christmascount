const express = require('express')
const http = require('http')
const cors = require('cors')

const assert = require('assert');

const MongoClient = require('mongodb').MongoClient
const mongoUrl = 'mongodb://mongo:27017'

const app = express()
app.use(cors())

let db

app.get('/speeches/:speechName', (req, res) => {
  const { speechName } = req.params
  const collection = db.collection(`${speechName}_global`)

  collection.findOne({key: 'global'}, (err, result) => {
    assert.equal(null, err)
    res.json(result)
  })

})

app.get('/speeches/:speechName/:word', (req, res) => {
  const { speechName, word } = req.params
  const collection = db.collection(`${speechName}_word`)

  collection.findOne({word}, (err, result) => {
    assert.equal(null, err)
    res.json(result)
  })

  }
)

const server = http.createServer(app);

const port = 4000
const host = '0.0.0.0'


MongoClient.connect(mongoUrl, (err, client) => {
  assert.equal(null, err)
  console.log('connected to database')
  db = client.db('speeches_count')

  server.listen({host, port}, () => console.log(`running on port ${port}`))

})

process.on('SIGINT', function() {
    process.exit();
});
