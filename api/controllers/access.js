const Validate = (req,res) => {
  let token = req.query.token
  if (token !== "thinkonce") {
    res.redirect('/')
  }
}

module.exports = {
  Validate
}
