
import { DisappearedLoading } from 'react-loadingg';
import NoInternet from './NoInternet'
import axios from 'axios';
import { Offline, Online } from "react-detect-offline";


import React from 'react';


class loading extends React.Component {

 

    render() {


        setTimeout(() => window.location = "./results", 50000);
        setTimeout(() => axios.get('https://sdgp-spoton-99.herokuapp.com/search/add/load/'), 5000);
        return (
            <div>
                {this.ShowAlertWithDelay}
                <Offline>        
                    <NoInternet></NoInternet>
                </Offline>
                
                <Online>                
                    <DisappearedLoading size="small"></DisappearedLoading>
                </Online>



            </div>

        )

    }
}


export default loading;