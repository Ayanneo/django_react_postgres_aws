import React, {useState, useEffect} from 'react';
// import notes from '../assets/data'
import Litstitem from '../components/Litstitem';
import AddButton from '../components/AddButton'

const NotesListPage = () => {

  const [notes, setNotes] = useState([]);

  // useEffect(() => {
  //   // Fetch notes from the API 
  //   fetch('http://localhost:8000/api/notes/')
  //     .then((response) => response.json())
  //     .then((data) => setNotes(data));
  // }, []);
  useEffect(() => {
    getNotes()
  }, []);

  let getNotes = async () => {
    let response = await fetch('/api/notes/')
    let data = await response.json()
    // console.log('data', data)
    setNotes(data)
  }

  return (
    <div className='notes'>

      <div className='notes-header'>
        <h2 className='notes-title'>Notes</h2>
        <p className='notes-count'>{notes.length}</p>
      </div>

        <div className='notes-list'>
            {notes.map((note, index)=>(
            <Litstitem key={index} note={note}/>
            ))}
        </div>
        
        <AddButton/>

    </div>
  )
}

export default NotesListPage