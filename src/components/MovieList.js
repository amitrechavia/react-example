import React from "react";
import Movie from "./Movie";
import { useEffect, useState } from 'react';


export default function MovieList({searchValue}) {
    const [data, setData] = useState([])
    //Onmount
    useEffect(() => {
        async function init() {
      //API Calls- request data from the server
        const response = await fetch('http://www.omdbapi.com/?apikey=ca0aa516&s=' + searchValue);
        const body = await response.json();
        setData(body);
     }
    init()
    
     }, [searchValue])

     console.log(data)
    if(data.Search) {
        return (
            <div className="container-fluid movie-app" >
                <div className="row">        
                    { 
                          data.Search.map((movie) => {    
                            return (
                                <Movie link={movie.Poster} />
                                )
                        })
                    } 
                </div>
            </div>          
        )
    }
   
    if(data?.Error?.includes('Incorrect ')) 
        return null
    
        return <p> {data.Error} </p>   
  }

