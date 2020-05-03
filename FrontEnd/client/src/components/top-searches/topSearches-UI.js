import React, { Component } from 'react';
import axios from 'axios';
import Fab from '@material-ui/core/Fab';
import Button from '@material-ui/core/Button';

/*This react component displays top trending searches today in the window Top
It fetches results from MongoDb and populates*/

//props which populates results from array
const TopSearch = props => (
    <div className="topTrendingRow-1">
        <Fab variant="extended" className="topTrendingRow-fab" style={{ cursor: 'default' }}>
            {props.topresults.query}
        </Fab>
        <br></br>
    </div>
)


//Class Top Searches
export default class TopSearches extends Component {
    constructor(props) {
        super(props);

        this.state = { results: [] }
    }


/*This Component runs first once the component is rendered
This is the best place to make API calls since, at this point, the component has been mounted and is available to the DOM*/

    componentDidMount() {
        axios.get('http://sdgp-spoton-99.herokuapp.com/todayTrends/')
            .then(response => {
                this.setState({ results: response.data })
                // console.log(se.username)
            })
            .catch((error) => {
                console.log(error)
            })
    }

//Mapping the results 
    resultList() {
        return this.state.results.map(currentSearch => {
            return <TopSearch topresults={currentSearch} key={currentSearch._id} />
        })
    }

//submit Functiom
    onSubmit(e) {
        e.preventDefault();
        window.location = '/spoton/top/subscribe';

    }

//Display to UI
    render() {
        return (
            <div>
                <br></br>
                <div className="topSearch-container">

                    <p className="main">Top</p>
                    <p className="heading">Trending Today</p>

                </div>
                <div>{this.resultList()}</div>
                <br></br>
                <div>
                    <h1 style={{ color: 'white' }}> Do You Want To Receive Hot Trending Topics?</h1>
                </div>
                <div className="subscribe-box">
                    <div style={{ padding: '30px' }}>
                        <Button variant="contained" color="secondary" onClick={e => this.onSubmit(e)} style={{ width: '160px', height: '40px' }}>
                            Subscribe
                    </Button>
                    </div>
                </div>


            </div>
        )
    }
}