import React from "react";



export default function SearchBox({searchValue, setSearchValue}) {
  //console.log(searchValue)
  return (
    <input
      type="text"
      placeholder="Type here"
      value={searchValue}
      onChange={(event) => setSearchValue(event.target.value)}
    />)
}

//setSearchValue(event.target.value)