//get links
window.onload = function () {
    fetch("/get-links").then((res) => {
      if (res.ok) {
        return res.json();
      } else {
        throw new Error("NETWORK RESPONSE ERROR");
      }
    })
    .then(data => {
      displayLinks(data)
    })
    .catch((error) => console.error("FETCH ERROR:", error)
    );
};
  //display links
function displayLinks(links) {
  links.forEach(link => {
    const card = `<div class="card" border-light mb-3" style="max-width: 18rem;">
    <div class="card-header">${(link.tag)}</div>
      <div class="card-body">
        <p class="card-text">${(link.description)}</p>
        <a href='${(link.url)}' rel="noopener noreferrer" target="_blank" class="btn btn-primary">Link Me!</a>
        <a href="/delete-link/${(link._id)['$oid']}" class="btn btn-primary">delete</a>
        <a href="/edit-link/${(link._id)['$oid']}" class="btn btn-primary">edit</a>
      </div>
    </div>`
    document.getElementById("links-list").insertAdjacentHTML('beforeend', card)
  });
};
// //delete note
// function addDeleteFunctionality () {
//   document.querySelectorAll("#delete_note").forEach(function(n) {
//     n.addEventListener("click", function() {
//       var id = this.getAttribute("data-id");
//       fetch("/delete-note", {
//         method: "POST",
//         body: JSON.stringify({ "noteId": id }),
//       }).then((_res) => {
//         window.location.href = "/";
//       });
//     });
//   });
// };
// //edit note
// function addEditFunctionality () {
//   document.querySelectorAll('#edit_note').forEach(function(e) {
//     e.addEventListener("click", function(){
//       var id = this.getAttribute("data-id");
//       var new_note = document.getElementById(id).value;
//       fetch("/edit_note", {
//         method: "PUT",
//         body: JSON.stringify({ "noteId": id, "newNote": new_note }),
//       }).then((_res) => {
//         window.location.href = "/";
//       });
//     });
//   });
// };