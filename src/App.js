import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Searchbox from "./components/SearchBox";
import Header from "./components/Header";
import Movie from "./components/Movie";
import MovieList from "./components/MovieList";
import MoviesJson from "./Movies.json"
import { useState } from 'react';

function App() {
  const [searchValue, setSearchValue] = useState('')
  return (
    <div className="App">
      <Header/>
      <Searchbox searchValue={searchValue} setSearchValue={setSearchValue} /> 
      <MovieList searchValue={searchValue}/>
    </div>
  );
}

export default App;

 // <MovieList searchValue={searchValue}/>