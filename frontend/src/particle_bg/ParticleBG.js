// import Particles from "react-particles";
import particlesConfig from "./particleBGConfig";

// const options = {
//           preset: "links",
//         };
// function ParticleBG() {
//     return (
//         <Particles options={particlesConfig}></Particles> 
//     );
// }
  
// export default ParticleBG;
import React from "react";
import Particles from "react-particles";
import type { Engine } from "tsparticles-engine";
import { loadLinksPreset } from "tsparticles-preset-links";

export class ParticleBG extends React.PureComponent<IProps> {
  // this customizes the component tsParticles installation
  async customInit(engine: Engine): Promise<void> {
    // this adds the preset to tsParticles, you can safely use the
    await loadLinksPreset(engine);
  }

  render() {
    const options = {
      preset: "links",
    };

    return <Particles options={particlesConfig} init={this.customInit} />;
  }
}

export default ParticleBG