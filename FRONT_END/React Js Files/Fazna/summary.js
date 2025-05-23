import React, { Component } from 'react';
import axios from 'axios';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import Typography from '@material-ui/core/Typography';

//constant which populates the Arrat based on the MongoDB Scheme Passed via Axios from Node js
const TopSearch = props => (
    <div className="topTrendingRow">
        <Card style={{ width: '30%', backgroundColor: 'transparent', color: 'white' }}>
            <CardContent>
                <Typography gutterBottom variant="h5" component="h2" style={{ textAlign: 'left', borderBottom: '1px solid white', paddingBottom: '3px', width: '45%', color: 'white' }}>
                    Text Summary
                         </Typography>
                <Typography variant="body2" component="p" style={{ textAlign: 'justify' }}>
                    {props.topresults.summary}

                </Typography>

            </CardContent>

        </Card>


    </div >
)

export default class ExercisesList extends Component {
    constructor(props) {
        super(props);


        this.state = { results: [] }


    }
    /*This Component runs first once the component is rendered
This is the best place to make API calls since, at this point, the component has been mounted and is available to the DOM*/

    componentDidMount() {
        axios.get('http://localhost:5000/search/results/summary')
            .then(response => {
                this.setState({ results: response.data })
                // console.log(se.username)
            })
            .catch((error) => {
                console.log(error)
            })
    }


    resultList() {
        return this.state.results.map(currentSearch => {
            return <TopSearch topresults={currentSearch} key={currentSearch._id} />
        })
    }


    render() {
        return (
            <div>

                <div>{this.resultList()}</div>

            </div>
        )
    }
}
