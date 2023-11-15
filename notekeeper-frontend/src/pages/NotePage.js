import React, {useState, useEffect} from 'react';
import { Link, useParams } from 'react-router-dom'
// import notes from '../assets/data'

// csrf token
// const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

const NotePage = () => {
  const noteId = useParams();
  let [note, setNote] = useState(null)
  // // console.log("id: ", noteId)
  // // console.log(typeof noteId)
  // // let note = notes.find(noteobj => {
  // //   return noteobj.id === Number(noteId)
  // // });

  // let note = notes.find(noteobj => {
  //   return noteobj.id === Number(noteId.id);
  // });

  // // console.log("notes: ", notes)
  // // console.log("note: ", note)

  useEffect(() => {
    getNote()
  }, [])

  let getNote = async () => {
    if (noteId.id === 'new') return
    let response = await fetch(`/api/notes/${noteId.id}`)
    let data = await response.json()
    console.log('data', data)
    setNote(data)
  }

  let createNote = async () => {
    fetch(`/api/notes/create/`, {
        method: "POST",
        headers: {
            'Content-Type': 'application/json',
            // 'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify(note)
    })
}

  const updateNote = async () => {
    try {
      const response = await fetch(`/api/notes/${noteId.id}/update/`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
          // 'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify(note),
      });
  
      if (!response.ok) {
        throw new Error(`Update failed with status: ${response.status}`);
      }
    } catch (error) {
      console.error('Error updating note:', error);
    }
  };

  let deleteNote = async () => {
    fetch(`/api/notes/${noteId.id}/delete/`, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
      },
    })
  }
  
  let handleSubmit = () => {
    if (noteId !== 'new' && note.body === '') {
      deleteNote()
  } else if (noteId !== 'new') {
      updateNote()
  }
  }

  return (
    <div className='note'>

      <div className='note-header'>
        <Link to="/">
            <h3 onClick={handleSubmit}>Back</h3>
        </Link>

        {noteId.id !== 'new' ? (
          <Link to="/">
            <button onClick={deleteNote}>Delete</button>
          </Link>
        ) : (<Link to="/"><button onClick={createNote}>Done</button></Link>)
        }
        
      </div>

      <textarea onChange={(e) => {setNote({...note, 'body': e.target.value})}} value={note?.body}>
      </textarea>

      {/* <p>{note?.body}</p> */}
    </div>
  )
}

export default NotePage