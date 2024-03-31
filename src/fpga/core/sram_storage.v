module sram_storage (
  input wire wr_en,
  
  input wire [16:0] addr,     // 128K words
  input wire [15:0] din,      // 8-bit input data (for ROM loading)
  output wire [15:0] dout,     // 8-bit output data 

  // -- sram bus parameters
  output wire [16:0] sram_a,
  inout wire [15:0] sram_dq,
  output wire sram_oe_n,
  output wire sram_we_n,
  output wire sram_ub_n,
  output wire sram_lb_n
);

assign sram_oe_n     = 1'b0;                  // Output always enabled
assign sram_we_n     = wr_en ? 1'b0 : 1'b1;          // write enable only applies when reset not held.
assign sram_ub_n     = 1'b0;                  // Always access high and low bytes.
assign sram_lb_n     = 1'b0;                  // 

assign sram_a        = addr;
assign sram_dq		   = wr_en ? din : {16{1'bZ}}; // Write when write-enabled; high-z when notreading

assign dout          = sram_dq;

endmodule
