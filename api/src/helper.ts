export function formatDate(d: Date) {
  const date = new Date(d);

  var day = ("0" + date.getDate()).slice(-2);
  var month = ("0" + (date.getMonth() + 1)).slice(-2);
  var year = date.getFullYear();

  return year + "-" + month + "-" + day;
}
