const fs = require("fs");
const path = require("path");

// This function can be used to recursively loop through a directory and output all documents that adhere to the given filter
// The filter implemented is the file extension
// It outputs a list and saves it under ./foundFiles.txt

function fromDir(startPath, filter) {
  if (!fs.existsSync(startPath)) {
    console.log(startPath, " is not a directory");
    return;
  }

  let foundFiles = [];
  var files = fs.readdirSync(startPath);
  for (const file of files) {
    var filename = path.join(startPath, file);
    var stat = fs.lstatSync(filename);
    if (stat.isDirectory()) {
      foundFiles = foundFiles.concat(fromDir(filename, filter)); //recurse
    } else if (filename.endsWith(filter)) {
      foundFiles.push(filename);
    }
  }
  return foundFiles;
}

let foundFiles = fromDir(
  "C:\\Users\\w111854\\OneDrive - Worldline\\DOKO test data\\Webgui\\Brown Bag Session\\Templates",
  ".png"
);

fs.writeFile("./filteredFiles.txt", JSON.stringify(foundFiles), (err) => {
  if (err) {
    console.log("Error writing .filteredFiles.txt", err);
  }
});
