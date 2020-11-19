import React, { Component } from "react";
import { withStyles } from "@material-ui/core/styles";
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";
import ConsensysLogoPath from "../media/consensys-logo.png";

const styles = theme => ({
  FooterContainer: {
    backgroundColor: "#fda941",
    marginTop: 40,
    padding: "80px 20px",
    color: 'white'
  },
  consensysLogo: {
    height: 60,
    width: 60
  },
  footerText: {
    color: 'inherit'
  }
})
class Footer extends Component {
  render() {
    const { classes } = this.props;
    
    return (
      <Grid container className={classes.FooterContainer}>
        
        <Grid item xs={12} sm={6}>
          <Grid container alignItems="center" justify="center" style={{height: '100%'}}>
            <img src={ConsensysLogoPath} alt="ConsenSys" className={classes.consensysLogo}/>
            <Typography variant="display1" style={{marginLeft: 10, fontSize: '1.6em', color: 'inherit'}}>ConsenSys Academy 2018</Typography>
          </Grid>
        </Grid>
        <Grid item xs={12} sm={6}>
          <Grid container justify="center" alignItems="center">
            <div>
              <Typography className={classes.footerText}>Linkedin: <a target="_blank" rel="noopener noreferrer" href="https://www.linkedin.com/in/andrew-saintway">Andrew Saintway</a></Typography>
              <Typography className={classes.footerText}>Github: <a target="_blank" rel="noopener noreferrer" href="https://github.com/seii-saintway">@seii-saintway</a></Typography>
              <Typography className={classes.footerText}>Twitter: <a target="_blank" rel="noopener noreferrer" href="https://twitter.com/seii_saintway">@seii_saintway</a></Typography>
              <Typography className={classes.footerText}>Github Repository: <a target="_blank" rel="noopener noreferrer" href="https://github.com/seii-saintway/patronsaint">Patronsaint</a></Typography>
            </div>
          </Grid>
        </Grid>
      </Grid>
    )
  }
}

export default withStyles(styles)(Footer);
