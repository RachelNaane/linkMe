//get notes
window.onload = function () {
    fetch("/get-notes").then((res) => {
      if (res.ok) {
        return res.json();
      } else {
        throw new Error("NETWORK RESPONSE ERROR");
      }
    })
    .then(data => {
      displayNotes(data)
    })
    .catch((error) => console.error("FETCH ERROR:", error)
    );
};
  //display notes
function displayNotes(notes) {
  notes.forEach(note => {
    const li = `<li class="list-group-item">
      <input type="text" id="${(note._id)['$oid']}" value="${note.text}" class="border-0">
      <button type="button" id ="delete_note" class="close" data-id="${(note._id)['$oid']}">
        <span aria-hidden="true">&times;</span>
      </button>
      <button type="button" id ="edit_note" class="close" data-id="${(note._id)['$oid']}">
        <span aria-hidden="true">&#9998;</span>
      </button>
      </li>`
    document.getElementById("notes").insertAdjacentHTML('beforeend', li)
  });
  addDeleteFunctionality();
  addEditFunctionality();
};
//delete note
function addDeleteFunctionality () {
  document.querySelectorAll("#delete_note").forEach(function(n) {
    n.addEventListener("click", function() {
      var id = this.getAttribute("data-id");
      fetch("/delete-note", {
        method: "POST",
        body: JSON.stringify({ "noteId": id }),
      }).then((_res) => {
        window.location.href = "/";
      });
    });
  });
};
//edit note
function addEditFunctionality () {
  document.querySelectorAll('#edit_note').forEach(function(e) {
    e.addEventListener("click", function(){
      var id = this.getAttribute("data-id");
      var new_note = document.getElementById(id).value;
      fetch("/edit_note", {
        method: "PUT",
        body: JSON.stringify({ "noteId": id, "newNote": new_note }),
      }).then((_res) => {
        window.location.href = "/";
      });
    });
  });
};